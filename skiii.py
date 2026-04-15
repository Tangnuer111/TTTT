#!/usr/bin/env python3
"""
skiii - AI辅助编程学习工具
面向大学生，利用 AI 代码辅助工具学习算法知识点
"""

import sys
import os

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from interactive import InteractiveLearner
from topics import TOPICS
from ai_adapter import AIAdapter


def print_banner():
    banner = """
╔═══════════════════════════════════════════════════╗
║                                                   ║
║     ████████╗██╗  ██╗███████╗                     ║
║     ╚══██╔══╝██║  ██║██╔════╝                     ║
║        ██║   ███████║█████╗                       ║
║        ██║   ██╔══██║██╔══╝                       ║
║        ██║   ██║  ██║███████╗                     ║
║        ╚═╝   ╚═╝  ╚═╝╚══════╝                     ║
║                                                   ║
║   AI辅助编程学习工具 | v0.1 原型                    ║
╚═══════════════════════════════════════════════════╝
    """
    print(banner)


def print_topics():
    print("\n📚 选择要学习的知识点：\n")
    for i, topic in enumerate(TOPICS, 1):
        print(f"  [{i}] {topic['icon']} {topic['name']}")
        print(f"      {topic['desc']}\n")


def main():
    print_banner()

    # 检查 API Key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if api_key:
        print("✅ 已检测到 ANTHROPIC_API_KEY，AI 辅助已启用\n")
        ai = AIAdapter(api_key)
    else:
        print("⚠️  未检测到 ANTHROPIC_API_KEY，将使用本地讲解模式")
        print("   如需 AI 辅助，请设置环境变量：export ANTHROPIC_API_KEY=your_key\n")
        ai = None

    print_topics()

    choice = input("请输入选项编号 (直接回车退出): ").strip()

    if not choice:
        print("\n👋 下次见！")
        return

    try:
        idx = int(choice) - 1
        if idx < 0 or idx >= len(TOPICS):
            raise ValueError()
        topic = TOPICS[idx]
    except ValueError:
        print("❌ 无效选项")
        return

    print(f"\n🚀 开始学习: {topic['name']}\n")
    learner = InteractiveLearner(topic, ai)
    learner.run()


if __name__ == "__main__":
    main()
