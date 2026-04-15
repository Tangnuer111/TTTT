"""
交互式学习引擎
"""

import os
import sys
from topics import get_topic_data


class InteractiveLearner:
    """交互式学习器"""

    def __init__(self, topic: dict, ai_adapter=None):
        self.topic = topic
        self.ai = ai_adapter
        self.topic_data = get_topic_data(topic["id"])

    def run(self):
        """运行学习流程"""
        self._show_menu()

        while True:
            choice = input("\n请选择 (0-4): ").strip()

            if choice == "0":
                print("\n👋 学习结束，祝你编程愉快！")
                break
            elif choice == "1":
                self._learn_theory()
            elif choice == "2":
                self._show_examples()
            elif choice == "3":
                self._do_practice()
            elif choice == "4":
                self._ask_ai()
            else:
                print("❌ 无效选项，请重新输入")

    def _show_menu(self):
        menu = f"""
╔═══════════════════════════════════════════════════╗
║  📖 {self.topic['name']} - 学习菜单                     ║
╚═══════════════════════════════════════════════════╝

  [1] 📚 学习理论
  [2] 💻 查看示例代码
  [3] ✍️  做练习题
  [4] 🤖  向 AI 提问
  [0] 🚪 退出
"""
        print(menu)

    def _learn_theory(self):
        """学习理论"""
        theory_list = self.topic_data.get("theory", [])

        print(f"\n{'='*50}")
        print(f"📚 {self.topic['name']} 理论知识")
        print('='*50)

        for i, theory in enumerate(theory_list, 1):
            print(f"\n--- 第 {i} 部分 ---\n")
            print(theory)

        input("\n按回车键返回菜单...")

    def _show_examples(self):
        """查看示例"""
        print(f"\n{'='*50}")
        print(f"💻 {self.topic['name']} 示例代码")
        print('='*50)

        theory_list = self.topic_data.get("theory", [])

        # 从理论中提取代码块
        import re
        for i, theory in enumerate(theory_list):
            # 简单提取 ```python ... ``` 块
            code_blocks = re.findall(r'```python\n(.*?)```', theory, re.DOTALL)
            for j, code in enumerate(code_blocks, 1):
                print(f"\n--- 示例 {i}.{j} ---")
                print(code)

        print(f"\n{'='*50}")
        print("💡 提示: 你可以复制这些代码到本地运行测试")
        print('='*50)

        input("\n按回车键返回菜单...")

    def _do_practice(self):
        """做练习"""
        practice = self.topic_data.get("practice", "暂无练习题")

        print(f"\n{'='*50}")
        print(f"✍️  {self.topic['name']} 练习题")
        print('='*50)
        print(practice)

        print("\n" + "="*50)
        print("📝 提交你的答案")
        print("="*50)

        user_code = self._get_multiline_input()

        if user_code.strip():
            print("\n📤 正在提交答案...")

            if self.ai and self.ai.is_available():
                print("\n🤖 AI 正在审阅你的答案...\n")
                review = self.ai.review_solution(
                    user_code,
                    self.topic["name"],
                    practice
                )
                print(review)
            else:
                print("\n💡 建议检查:")
                print("   1. 代码逻辑是否正确")
                print("   2. 边界条件是否处理")
                print("   3. 可以设置 ANTHROPIC_API_KEY 获取 AI 审阅")

        input("\n按回车键返回菜单...")

    def _ask_ai(self):
        """向 AI 提问"""
        if not self.ai or not self.ai.is_available():
            print("\n⚠️  AI 辅助暂不可用")
            print("   请设置 ANTHROPIC_API_KEY 环境变量")
            print("   export ANTHROPIC_API_KEY=your_key\n")
            return

        print("\n🤖 AI 辅导模式 (输入 'q' 退出)")
        print("-"*40)

        while True:
            question = input("\n❓ 你想问什么: ").strip()

            if question.lower() == 'q':
                break

            if not question:
                continue

            print("\n🤖 AI 思考中...\n")

            answer = self.ai.answer_question(
                question,
                self.topic["name"]
            )

            print(answer)

    def _get_multiline_input(self) -> str:
        """获取多行输入"""
        print("(输入 'END' 结束输入)")
        lines = []
        while True:
            line = input()
            if line.strip() == 'END':
                break
            lines.append(line)
        return '\n'.join(lines)
