from __future__ import annotations

"""RAG 主流程编排模块。

职责：
1. 将文档加载、切块、向量化、索引构建串联为 `build_index()`；
2. 将查询处理、检索、提示词构造、生成串联为 `ask()`；
3. 管理短期会话记忆，支持后续扩展。
"""

from dataclasses import dataclass

from embedder import SentenceTransformerEmbedder
from generator import LLMGenerator
from loader import DocumentLoader
from memory import BaseMemory, InMemoryHistory
from prompt_builder import PromptBuilder
from query_processor import QueryProcessor
from splitter import TextSplitter
from vector_store import ChunkRecord, VectorStore


@dataclass
class AskResult:
    """问答结果结构。

    字段说明：
    - `answer`: 最终回答；
    - `prompt`: 发送给模型的完整提示词（便于调试）；
    - `citations`: 引用片段信息列表。
    """

    answer: str
    prompt: str
    citations: list[dict]


class RAGPipeline:
    """可插拔的 RAG 流程对象。

    所有组件都支持依赖注入，便于测试和扩展。
    """

    def __init__(
        self,
        loader: DocumentLoader | None = None,
        splitter: TextSplitter | None = None,
        embedder: SentenceTransformerEmbedder | None = None,
        store: VectorStore | None = None,
        query_processor: QueryProcessor | None = None,
        prompt_builder: PromptBuilder | None = None,
        generator: LLMGenerator | None = None,
        memory: BaseMemory | None = None,
    ):
        """初始化流程组件。

        输入：
        - 各模块实例（可选）；若不传，使用默认实现。
        """
        self.loader = loader or DocumentLoader(md_dir="md_data", fallback_file="data/docs.txt")
        self.splitter = splitter or TextSplitter(chunk_size=700, overlap=100)
        self.embedder = embedder or SentenceTransformerEmbedder()
        self.store = store or VectorStore(store_dir="data/vector_store")
        self.query_processor = query_processor or QueryProcessor()
        self.prompt_builder = prompt_builder or PromptBuilder()
        self.generator = generator or LLMGenerator()
        self.memory = memory or InMemoryHistory()

    def build_index(self) -> dict:
        """构建并保存向量索引。

        流程：
        - 文档加载 -> 分块 -> 向量化 -> 向量库 build/save。

        输出：
        - `dict`，向量库统计信息（documents/chunks/dim）。
        """
        docs = self.loader.load()
        chunks = []
        for doc in docs:
            chunks.extend(self.splitter.split(doc.doc_id, doc.source, doc.text))

        texts = [c.text for c in chunks]
        vectors = self.embedder.encode(texts)
        records = [ChunkRecord(c.chunk_id, c.doc_id, c.source, c.text) for c in chunks]

        self.store.build(vectors, records)
        self.store.save()
        return self.store.stats()

    def load_index(self) -> None:
        """从磁盘加载历史向量索引。"""
        self.store.load()

    def ask(self, question: str, top_k: int = 5) -> AskResult:
        """执行一次 RAG 问答。

        输入：
        - `question`: 用户原始问题；
        - `top_k`: 检索返回条数。

        输出：
        - `AskResult`，包含回答、prompt 和引用信息。
        """
        q = self.query_processor.process(question)
        query_vec = self.embedder.encode([q])
        retrieved = self.store.search(query_vec, top_k=top_k)

        mem_lines = [f"{r}: {c}" for r, c in self.memory.recent(limit=6)]
        memory_text = "\n".join(mem_lines)
        prompt = self.prompt_builder.build(q, retrieved, memory_text=memory_text)
        answer = self.generator.generate(prompt)

        self.memory.append("user", question)
        self.memory.append("assistant", answer)

        citations = [{"source": c.source, "chunk_id": c.chunk_id, "score": s} for c, s in retrieved]
        return AskResult(answer=answer, prompt=prompt, citations=citations)
