"""
AI 适配器 - 预留 Claude API 接口
当设置 ANTHROPIC_API_KEY 环境变量后，可以调用 Claude 进行 AI 辅助
"""

import os
import anthropic


class AIAdapter:
    """AI 适配器，支持 Claude API 调用"""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        self.client = None
        if self.api_key:
            self.client = anthropic.Anthropic(api_key=self.api_key)

    def is_available(self) -> bool:
        """检查 AI 是否可用"""
        return self.client is not None

    def explain_code(self, code: str, context: str = "") -> str:
        """解释代码"""
        if not self.is_available():
            return self._local_explain(code, context)

        response = self.client.messages.create(
            model="claude-sonnet-4-6-20250514",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": f"请解释以下代码的功能和工作原理:\n\n```{context}\n{code}\n```"
                }
            ]
        )
        return response.content[0].text

    def debug_code(self, code: str, error: str = "") -> str:
        """调试代码"""
        if not self.is_available():
            return self._local_debug(code, error)

        error_context = f"\n错误信息:\n{error}" if error else ""

        response = self.client.messages.create(
            model="claude-sonnet-4-6-20250514",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": f"请帮我调试以下代码，找出 bug 并给出修复建议:\n\n```{error_context}\n{code}\n```"
                }
            ]
        )
        return response.content[0].text

    def answer_question(self, question: str, topic: str = "") -> str:
        """回答学习相关问题"""
        if not self.is_available():
            return f"本地模式: {question}\n\n(设置 ANTHROPIC_API_KEY 环境变量以获取 AI 辅导)"

        topic_context = f"当前学习主题: {topic}" if topic else ""

        response = self.client.messages.create(
            model="claude-sonnet-4-6-20250514",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": f"{topic_context}\n\n问题: {question}\n\n请用简洁易懂的方式回答，适合大学生理解。"
                }
            ]
        )
        return response.content[0].text

    def review_solution(self, code: str, topic: str, exercise: str) -> str:
        """审阅解题方案"""
        if not self.is_available():
            return self._local_review(code)

        response = self.client.messages.create(
            model="claude-sonnet-4-6-20250514",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": f"主题: {topic}\n\n练习题:\n{exercise}\n\n学生的解答:\n```{code}\n```\n\n请审阅这个解答，给出评价和改进建议:"
                }
            ]
        )
        return response.content[0].text

    # 本地 fallback 方法
    def _local_explain(self, code: str, context: str) -> str:
        return f"""本地讲解模式:
代码片段:
{code}

(设置 ANTHROPIC_API_KEY 环境变量以获取详细 AI 讲解)"""

    def _local_debug(self, code: str, error: str) -> str:
        return f"""本地调试提示:
错误信息: {error}

常见排查步骤:
1. 检查变量是否正确初始化
2. 确认索引是否越界
3. 验证数据类型是否匹配

(设置 ANTHROPIC_API_KEY 环境变量以获取详细 AI 调试帮助)"""

    def _local_review(self, code: str) -> str:
        return f"""本地审阅模式:
您的代码:
{code}

建议:
1. 检查边界条件
2. 确认算法逻辑是否正确
3. 考虑是否有更优解法

(设置 ANTHROPIC_API_KEY 环境变量以获取详细代码审阅)"""
