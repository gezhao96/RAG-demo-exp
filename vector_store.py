from __future__ import annotations

"""向量库存储与检索模块。

职责：
1. 维护向量矩阵和分块元数据；
2. 提供本地持久化（`.npy` + `.json`）；
3. 提供基于向量点积的 Top-K 检索。

输入：
- `build()`：向量矩阵 + `ChunkRecord` 列表；
- `search()`：查询向量 + `top_k`。

输出：
- 检索结果：`list[(ChunkRecord, score)]`。
"""

from dataclasses import asdict, dataclass
import json
from pathlib import Path

import numpy as np


@dataclass
class ChunkRecord:
    """向量库中的分块记录结构。"""

    chunk_id: str
    doc_id: str
    source: str
    text: str


class VectorStore:
    """本地文件型向量库。"""

    def __init__(self, store_dir: str = "data/vector_store"):
        """初始化向量库路径与内存状态。"""
        self.store_dir = Path(store_dir)
        self.store_dir.mkdir(parents=True, exist_ok=True)
        self.vec_file = self.store_dir / "vectors.npy"
        self.meta_file = self.store_dir / "metadata.json"
        self.vectors = np.zeros((0, 1), dtype=np.float32)
        self.metadata: list[ChunkRecord] = []

    def build(self, vectors: np.ndarray, records: list[ChunkRecord]) -> None:
        """构建（或替换）内存中的向量索引。

        输入：
        - `vectors`: 分块向量矩阵 `(N, dim)`；
        - `records`: 与向量一一对应的元数据列表。
        """
        if vectors.ndim == 1:
            vectors = vectors.reshape(1, -1)
        self.vectors = vectors.astype(np.float32)
        self.metadata = records

    def save(self) -> None:
        """将向量和元数据保存到磁盘。"""
        np.save(self.vec_file, self.vectors)
        self.meta_file.write_text(
            json.dumps([asdict(m) for m in self.metadata], ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def load(self) -> None:
        """从磁盘加载向量和元数据到内存。"""
        if self.vec_file.exists() and self.meta_file.exists():
            self.vectors = np.load(self.vec_file)
            raw = json.loads(self.meta_file.read_text(encoding="utf-8"))
            self.metadata = [ChunkRecord(**x) for x in raw]

    def search(self, query_vec: np.ndarray, top_k: int = 5) -> list[tuple[ChunkRecord, float]]:
        """检索与查询最相似的 Top-K 分块。

        输入：
        - `query_vec`: 查询向量，形状 `(dim,)` 或 `(1, dim)`；
        - `top_k`: 返回条数。

        输出：
        - `[(ChunkRecord, score), ...]`，按相似度降序。
        """
        if self.vectors.size == 0 or query_vec.size == 0:
            return []
        if query_vec.ndim == 2:
            query_vec = query_vec[0]
        sims = self.vectors @ query_vec
        idx = np.argsort(-sims)[:top_k]
        return [(self.metadata[i], float(sims[i])) for i in idx]

    def stats(self) -> dict:
        """返回向量库统计信息。"""
        return {
            "documents": len({m.doc_id for m in self.metadata}),
            "chunks": len(self.metadata),
            "dim": int(self.vectors.shape[1]) if self.vectors.size else 0,
        }
