# RAG (Retrieval-Augmented Generation)

一个便于扩展的标准 Python RAG 项目（单体结构）。

## 目录结构

```text
RAG/
├── data/
│   ├── docs.txt
│   └── vector_store/
├── md_data/
├── loader.py
├── splitter.py
├── embedder.py
├── vector_store.py
├── query_processor.py
├── prompt_builder.py
├── generator.py
├── rag_pipeline.py
├── memory.py
├── app.py
└── requirements.txt
```

## 快速开始

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
pip install -r requirements.txt
```

可选环境变量（OpenAI 兼容接口）：

```env
OPENAI_API_KEY=
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL=gpt-4o-mini
```

运行：

```bash
python app.py
```

默认会优先加载 `md_data/*.md`，如果没有文档则回退到 `data/docs.txt`。

## 可扩展建议

- 新增记忆模块：继承 `memory.py` 中 `BaseMemory` 协议。
- 替换向量库：实现与 `VectorStore` 类似的 `build/save/load/search` 行为。
- 替换大模型：修改 `generator.py` 的 `LLMGenerator`。
