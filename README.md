# skiii - AI辅助编程学习工具

面向在校大学生的算法学习 CLI 工具。

## 功能特点

- 📚 **知识点学习** - 排序算法、二分查找、链表、栈与队列
- 💻 **理论 + 示例** - 每个知识点包含详细讲解和可运行代码
- ✍️ **练习题** - 边学边练，巩固知识
- 🤖 **AI 辅助** - 接入 Claude API，获取代码讲解、调试和审阅

## 快速开始

### 1. 安装依赖

```bash
cd skiii
pip install -r requirements.txt
```

### 2. (可选) 设置 AI 辅助

```bash
# Linux/Mac
export ANTHROPIC_API_KEY=your_api_key

# Windows (CMD)
set ANTHROPIC_API_KEY=your_api_key

# Windows (PowerShell)
$env:ANTHROPIC_API_KEY="your_api_key"
```

### 3. 运行

```bash
python skiii.py
```

## 使用流程

```
1. 启动后选择要学习的知识点
2. 选择 [1] 学习理论 - 阅读知识点讲解
3. 选择 [2] 查看示例 - 复制运行示例代码
4. 选择 [3] 做练习 - 完成练习题并提交
5. 选择 [4] 向 AI 提问 - 获得个性化辅导
```

## 项目结构

```
skiii/
├── skiii.py           # 主入口
├── interactive.py     # 交互式学习引擎
├── ai_adapter.py      # AI 适配器 (Claude API)
├── config.py          # 配置文件
├── topics/            # 知识点模块
│   ├── __init__.py
│   ├── sorting.py     # 排序算法
│   ├── binary_search.py  # 二分查找
│   ├── linked_list.py    # 链表
│   └── stack_queue.py    # 栈与队列
└── requirements.txt
```

## 获取 Claude API Key

1. 访问 [Anthropic Console](https://console.anthropic.com/)
2. 注册/登录账号
3. 在 API Keys 页面创建新的 API Key
4. 将 Key 设置为环境变量

## 扩展知识点

在 `topics/` 目录下创建新的 Python 文件即可添加新的知识点:

```python
# topics/my_topic.py

CONTENT = """
## 我的知识点

### 内容...
"""

PRACTICE = """
## 练习题...
"""

def get_data():
    return {
        "theory": [CONTENT],
        "practice": PRACTICE,
    }
```

然后在 `topics/__init__.py` 中注册即可。
