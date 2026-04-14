from __future__ import annotations

"""文本切块模块。

职责：
- 将长文本按固定窗口切分为重叠分块（chunk），便于向量化和检索。

输入：
- 文档标识、来源和正文文本。

输出：
- `list[Chunk]`，每个分块携带 `chunk_id/doc_id/source/text`。
"""

from dataclasses import dataclass


@dataclass
class Chunk:
    """分块数据结构。

    字段说明：
    - `chunk_id`: 形如 `doc_id:index`；
    - `doc_id`: 所属文档 ID；
    - `source`: 文档来源；
    - `text`: 当前分块文本。
    """

    chunk_id: str
    doc_id: str
    source: str
    text: str


class TextSplitter:
    """滑动窗口切块器。

    参数：
    - `chunk_size`: 每块字符长度上限；
    - `overlap`: 相邻分块重叠长度，避免语义截断。
    """

    def __init__(self, chunk_size: int = 700, overlap: int = 100):
        if overlap >= chunk_size:
            raise ValueError("overlap must be smaller than chunk_size")
        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(self, doc_id: str, source: str, text: str) -> list[Chunk]:
        """对单篇文档进行切块。

        输入：
        - `doc_id`: 文档 ID；
        - `source`: 文档来源；
        - `text`: 文档全文。

        输出：
        - `list[Chunk]`。
        """
        chunks: list[Chunk] = []
        n = len(text)
        start = 0
        idx = 0
        while start < n:
            end = min(n, start + self.chunk_size)
            piece = text[start:end].strip()
            if piece:
                chunks.append(Chunk(chunk_id=f"{doc_id}:{idx}", doc_id=doc_id, source=source, text=piece))
                idx += 1
            if end == n:
                break
            start = max(end - self.overlap, start + 1)
        return chunks
