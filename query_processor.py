from __future__ import annotations

"""查询处理模块。

职责：
- 对用户问题做规范化与可扩展改写，给检索模块更稳定的输入。
"""

import re


class QueryProcessor:
    """查询处理模块：可用于清洗、改写、扩展关键词。"""

    def normalize(self, query: str) -> str:
        """基础清洗。

        输入：
        - `query`: 原始查询字符串。

        输出：
        - 去除首尾空白并压缩连续空白后的查询。
        """
        query = query.strip()
        query = re.sub(r"\s+", " ", query)
        return query

    def expand(self, query: str) -> str:
        """查询扩展。

        输入：
        - `query`: 规范化后的查询。

        输出：
        - 当前版本直接原样返回。
        - 可扩展为同义词扩展、纠错、实体补全、意图改写等。
        """
        # 预留扩展点：可接入同义词、拼写纠错、意图识别。
        return query

    def process(self, query: str) -> str:
        """处理入口，串联 normalize + expand。"""
        q = self.normalize(query)
        return self.expand(q)
