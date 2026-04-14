from __future__ import annotations

"""大模型生成模块。

职责：
- 接收 prompt，调用 OpenAI 兼容接口返回回答；
- 在未配置密钥或请求失败时提供可用的 fallback 响应。
"""

import os
import logging

logger = logging.getLogger(__name__)


class LLMGenerator:
    """LLM 生成器。"""

    def __init__(self):
        """从环境变量读取模型配置。"""
        self.api_key = os.getenv("OPENAI_API_KEY", "")
        self.base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
        self.model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    def _fallback(self, prompt: str) -> str:
        """降级响应。

        输入：
        - `prompt`: 构造后的完整提示词。

        输出：
        - fallback 文本，便于调试链路。
        """
        return (
            "[Fallback Answer]\n"
            "OPENAI_API_KEY is not configured or model request failed.\n"
            "Below is the prompt summary for manual inspection:\n\n"
            f"{prompt[:1200]}"
        )

    def generate(self, prompt: str) -> str:
        """调用模型生成回答。

        输入：
        - `prompt`: PromptBuilder 输出的提示词。

        输出：
        - 模型生成文本；失败时返回 `_fallback`。
        """
        if not self.api_key:
            return self._fallback(prompt)

        try:
            import httpx

            with httpx.Client(timeout=60.0) as client:
                resp = client.post(
                    f"{self.base_url}/chat/completions",
                    headers={"Authorization": f"Bearer {self.api_key}"},
                    json={
                        "model": self.model,
                        "messages": [{"role": "user", "content": prompt}],
                        "temperature": 0.2,
                    },
                )
                resp.raise_for_status()
                data = resp.json()
                return data["choices"][0]["message"]["content"]
        except Exception as exc:
            logger.warning("LLM request failed: %s", exc)
            return self._fallback(prompt)
