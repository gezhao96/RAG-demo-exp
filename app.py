from __future__ import annotations

"""主程序入口模块。

职责：
- 初始化日志；
- 构建索引；
- 以命令行交互方式执行问答并展示引用来源。

输入：
- 终端用户输入问题。

输出：
- 控制台打印回答和 citations。
"""

import logging
import os

from dotenv import load_dotenv

os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

load_dotenv()

from rag_pipeline import RAGPipeline


def main() -> None:
    """CLI 主函数。"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    pipeline = RAGPipeline()
    stats = pipeline.build_index()
    print(f"Index ready: docs={stats['documents']} chunks={stats['chunks']} dim={stats['dim']}")

    while True:
        # 输入/退出逻辑
        q = input("\nQuestion (输入 exit 退出) > ").strip()
        if not q:
            continue
        if q.lower() in {"exit", "quit"}:
            break

        # 问答执行与结果展示
        result = pipeline.ask(q, top_k=5)
        print("\n=== Answer ===")
        print(result.answer)
        print("\n=== Citations ===")
        for c in result.citations:
            print(f"- {c['source']} | {c['chunk_id']} | score={c['score']:.4f}")


if __name__ == "__main__":
    main()
