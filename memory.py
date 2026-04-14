from __future__ import annotations

"""记忆模块。

职责：
- 定义统一记忆抽象 `BaseMemory`；
- 提供默认内存实现 `InMemoryHistory`。

扩展方向：
- 可替换为持久化记忆、向量记忆、用户画像记忆等。
"""

from dataclasses import dataclass, field
from abc import ABC, abstractmethod


class BaseMemory(ABC):
    """可扩展记忆接口，后续可替换为向量记忆/会话记忆。"""

    @abstractmethod
    def append(self, role: str, content: str) -> None:
        """追加一条对话记录。

        输入：
        - `role`: 角色（如 `user` / `assistant`）；
        - `content`: 对话文本。
        """
        raise NotImplementedError

    @abstractmethod
    def recent(self, limit: int = 6) -> list[tuple[str, str]]:
        """读取最近对话。

        输入：
        - `limit`: 返回条数上限。

        输出：
        - 列表元素为 `(role, content)`。
        """
        raise NotImplementedError


@dataclass
class InMemoryHistory(BaseMemory):
    """基于 Python 列表的轻量记忆实现。"""

    items: list[tuple[str, str]] = field(default_factory=list)

    def append(self, role: str, content: str) -> None:
        self.items.append((role, content))

    def recent(self, limit: int = 6) -> list[tuple[str, str]]:
        return self.items[-limit:]
