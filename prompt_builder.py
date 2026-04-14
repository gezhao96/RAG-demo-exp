from __future__ import annotations

"""提示词拼接模块。

职责：
- 将“问题 + 检索结果 + 会话记忆”拼接成结构化 prompt，供大模型生成使用。
"""

from vector_store import ChunkRecord


class PromptBuilder:
    """Prompt 构造器。"""

    def build(self, question: str, retrieved: list[tuple[ChunkRecord, float]], memory_text: str = "") -> str:
        """构造最终生成提示词。

        输入：
        - `question`: 处理后的用户问题；
        - `retrieved`: 检索结果，元素为 `(ChunkRecord, score)`；
        - `memory_text`: 历史对话摘要文本（可空）。

        输出：
        - `str`，可直接传给大模型的 prompt。
        """
        context_blocks = []
        for idx, (chunk, score) in enumerate(retrieved, start=1):
            context_blocks.append(
                f"[Context {idx}] source={chunk.source} chunk_id={chunk.chunk_id} score={score:.4f}\n{chunk.text}"
            )

        context_text = "\n\n".join(context_blocks) if context_blocks else "(no retrieved context)"
        memory_section = f"\n\nConversation Memory:\n{memory_text}\n" if memory_text else ""

        return (
            "You are a helpful RAG assistant. Answer only based on retrieved context. "
            "If context is insufficient, explicitly say you are not sure.\n\n"
            f"Question:\n{question}\n"
            f"{memory_section}\n"
            f"Retrieved Context:\n{context_text}\n\n"
            "Return a concise and factual answer."
        )
