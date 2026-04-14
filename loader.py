from __future__ import annotations

"""文档加载模块。

职责：
1. 从 `md_data` 目录读取 Markdown 文档；
2. 清洗 Markdown 标记，输出适合向量化的纯文本；
3. 当 `md_data` 为空时，回退读取 `data/docs.txt`。

输入：
- 文件系统路径（由 `md_dir` 和 `fallback_file` 指定）。

输出：
- `list[Document]`，每个对象包含 `doc_id/source/text`。
"""

from dataclasses import dataclass
from pathlib import Path
import re


@dataclass
class Document:
    """标准化文档结构。

    字段说明：
    - `doc_id`: 文档唯一标识，后续用于 chunk_id 构造；
    - `source`: 文档来源（通常是文件名）；
    - `text`: 清洗后的正文文本。
    """

    doc_id: str
    source: str
    text: str


class DocumentLoader:
    """文档加载器。

    输入：
    - `md_dir`: Markdown 数据目录；
    - `fallback_file`: 回退文件路径。

    输出：
    - 通过 `load()` 返回 `list[Document]`。
    """

    def __init__(self, md_dir: str = "md_data", fallback_file: str = "data/docs.txt"):
        self.md_dir = Path(md_dir)
        self.fallback_file = Path(fallback_file)

    @staticmethod
    def _clean_markdown(text: str) -> str:
        """将 Markdown 文本清洗为纯文本。

        输入：
        - `text`: 原始 Markdown 文本。

        输出：
        - 清洗后文本（移除代码块、行内代码、链接、图片、部分标记）。
        """
        text = re.sub(r"```[\s\S]*?```", " ", text)
        text = re.sub(r"`[^`]*`", " ", text)
        text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
        text = re.sub(r"\[[^\]]*\]\([^)]*\)", " ", text)
        text = re.sub(r"^[#>*-]+", "", text, flags=re.MULTILINE)
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    def load(self) -> list[Document]:
        """读取并返回文档列表。

        执行顺序：
        1. 优先读取 `md_dir/*.md`；
        2. 若没有可用文档，则尝试 `fallback_file`；
        3. 两者都不可用时返回空列表。

        返回：
        - `list[Document]`。
        """
        docs: list[Document] = []

        if self.md_dir.exists():
            for path in sorted(self.md_dir.glob("*.md")):
                raw = path.read_text(encoding="utf-8", errors="ignore")
                clean = self._clean_markdown(raw)
                if clean:
                    docs.append(Document(doc_id=path.stem, source=path.name, text=clean))

        if docs:
            return docs

        if self.fallback_file.exists():
            raw = self.fallback_file.read_text(encoding="utf-8", errors="ignore")
            clean = self._clean_markdown(raw)
            if clean:
                docs.append(Document(doc_id="fallback-doc", source=str(self.fallback_file), text=clean))

        return docs
