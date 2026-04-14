# RAG (Retrieval-Augmented Generation)

一个便于扩展的标准 Python RAG 项目（单体结构），用于基于本地知识库的问答系统。

## 功能特性

- 📚 支持 Markdown 和文本格式文档加载
- 🔍 基于 sentence-transformers 的语义向量检索
- 🤖 支持 OpenAI 兼容接口（DeepSeek、通义千问等）
- 💾 本地向量存储，无需额外数据库
- 🔄 模块化设计，易于扩展

## 目录结构

```text
RAG/
├── data/
│   ├── docs.txt              # 备用文本文档
│   └── vector_store/         # 向量存储目录
├── md_data/                  # Markdown 文档目录（优先加载）
├── loader.py                 # 文档加载模块
├── splitter.py               # 文本分块模块
├── embedder.py               # 向量化模块
├── vector_store.py           # 向量存储模块
├── query_processor.py        # 查询处理模块
├── prompt_builder.py         # 提示词构建模块
├── generator.py              # LLM 生成模块
├── rag_pipeline.py           # RAG 主流程模块
├── memory.py                 # 对话记忆模块
├── app.py                    # 主程序入口
├── requirements.txt          # 依赖列表
└── .env                      # 环境变量配置（需自行创建）
```

## 快速开始

### 1. 创建虚拟环境

使用 conda（推荐）：
```bash
conda create -n rag python=3.11 -y
conda activate rag
```

或使用 venv：
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置环境变量

复制 `.env.example` 为 `.env`（如果没有的话直接创建）：

```env
OPENAI_API_KEY=your-api-key-here
OPENAI_BASE_URL=https://api.deepseek.com/v1
OPENAI_MODEL=deepseek-chat
```

**配置说明：**
- `OPENAI_API_KEY`: 你的 API 密钥（必需）
- `OPENAI_BASE_URL`: API 地址，支持 OpenAI 兼容接口
  - DeepSeek: `https://api.deepseek.com/v1`
  - OpenAI: `https://api.openai.com/v1`
- `OPENAI_MODEL`: 模型名称
  - DeepSeek: `deepseek-chat`
  - OpenAI: `gpt-4o-mini`

### 4. 准备文档

将你的 Markdown 文档放入 `md_data/` 目录，或文本内容放入 `data/docs.txt`。

### 5. 运行项目

```bash
python app.py
```

程序会自动：
1. 加载并解析文档
2. 构建向量索引
3. 启动交互式问答界面

使用示例：
```
Question (输入 exit 退出) > 什么是分布式光纤传感？

=== Answer ===
[AI 生成的回答...]

=== Citations ===
- 论文1.md | chunk-1 | score=0.8523
- 论文2.md | chunk-5 | score=0.7891
```

输入 `exit` 或 `quit` 退出程序。

## 模块说明

| 模块 | 职责 |
|------|------|
| `loader.py` | 从文件系统加载文档 |
| `splitter.py` | 将长文本切分为小块 |
| `embedder.py` | 文本向量化（支持 sentence-transformers 和 Hash  fallback） |
| `vector_store.py` | 向量存储和检索 |
| `query_processor.py` | 查询预处理 |
| `prompt_builder.py` | 构建 RAG 提示词 |
| `generator.py` | 调用 LLM 生成回答 |
| `rag_pipeline.py` | 串联整个 RAG 流程 |
| `memory.py` | 对话历史管理 |

## 可扩展建议

- **新增记忆模块**：继承 `memory.py` 中 `BaseMemory` 协议
- **替换向量库**：实现与 `VectorStore` 类似的 `build/save/load/search` 行为
- **替换大模型**：修改 `generator.py` 的 `LLMGenerator`
- **新增文档格式**：扩展 `loader.py` 支持更多格式（PDF、Word 等）

## 常见问题

### Q: HuggingFace 下载模型超时？
A: 设置镜像源：
```bash
# Linux/macOS
export HF_ENDPOINT=https://hf-mirror.com

# Windows PowerShell
$env:HF_ENDPOINT="https://hf-mirror.com"
```

### Q: 如何清空向量索引重新构建？
A: 删除 `data/vector_store/` 目录下的文件，重新运行 `python app.py`。

### Q: 支持哪些文档格式？
A: 默认支持 `.md`（Markdown）和 `.txt`（纯文本）。

## License

MIT License
