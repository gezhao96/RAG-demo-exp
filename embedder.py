from __future__ import annotations

"""向量化模块。

职责：
1. 提供统一向量化抽象 `BaseEmbedder`；
2. 提供轻量哈希向量实现 `HashEmbedder`（无外部模型依赖）；
3. 提供 `SentenceTransformerEmbedder`，并在模型不可用时自动降级。

输入：
- 文本列表 `list[str]`。

输出：
- `numpy.ndarray`，形状通常为 `(N, dim)`。
"""

import hashlib
import logging
from abc import ABC, abstractmethod

import numpy as np

logger = logging.getLogger(__name__)


class BaseEmbedder(ABC):
    """向量化器抽象基类。"""

    @abstractmethod
    def encode(self, texts: list[str]) -> np.ndarray:
        """将文本列表编码为向量矩阵。

        输入：
        - `texts`: 待编码文本列表。

        输出：
        - `np.ndarray`，维度为 `(len(texts), dim)`。
        """
        raise NotImplementedError


class HashEmbedder:
    """哈希向量化实现。

    适用场景：
    - 快速原型；
    - 无法安装模型依赖时的兜底方案。
    """

    def __init__(self, dim: int = 384):
        self.dim = dim

    def _one(self, text: str) -> np.ndarray:
        """将单条文本编码为单位化向量。"""
        vec = np.zeros(self.dim, dtype=np.float32)
        for token in text.lower().split():
            h = hashlib.sha256(token.encode("utf-8")).digest()
            idx = int.from_bytes(h[:4], "little") % self.dim
            vec[idx] += 1.0
        norm = np.linalg.norm(vec) + 1e-12
        return vec / norm

    def encode(self, texts: list[str]) -> np.ndarray:
        """批量哈希向量化。"""
        if not texts:
            return np.zeros((0, self.dim), dtype=np.float32)
        return np.vstack([self._one(t) for t in texts]).astype(np.float32)


class SentenceTransformerEmbedder:
    """基于 `sentence-transformers` 的语义向量化实现。"""

    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2", dim: int = 384):
        """初始化模型并准备降级策略。

        输入：
        - `model_name`: 模型名称；
        - `dim`: 向量维度（用于空输入和降级路径）。
        """
        self.dim = dim
        self.model = None
        self._fallback = HashEmbedder(dim=dim)
        try:
            from sentence_transformers import SentenceTransformer

            self.model = SentenceTransformer(model_name)
            logger.info("Loaded embedding model: %s", model_name)
        except Exception as exc:
            logger.warning("Embedding model load failed, fallback to HashEmbedder: %s", exc)

    def encode(self, texts: list[str]) -> np.ndarray:
        """批量编码文本，优先语义模型，失败时自动降级哈希向量。"""
        if not texts:
            return np.zeros((0, self.dim), dtype=np.float32)
        if self.model is None:
            return self._fallback.encode(texts)
        arr = self.model.encode(texts, normalize_embeddings=True)
        return np.asarray(arr, dtype=np.float32)
