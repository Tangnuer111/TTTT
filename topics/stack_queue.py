"""
栈与队列知识点
"""

STACK_CONTENT = """
## 栈 (Stack)

### 核心特性
**LIFO (Last In First Out)** - 后进先出

### 形象理解
像一摞盘子，最后放上去的盘子最先被拿走。

### 基本操作
- `push(x)` - 入栈，将元素放到栈顶
- `pop()` - 出栈，移除栈顶元素并返回
- `peek()` / `top()` - 查看栈顶元素
- `is_empty()` - 判断栈是否为空

### Python 实现
```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
```

### 应用场景
- 函数调用栈 (递归调用)
- 括号匹配
- 表达式求值 (中缀转后缀)
- 撤销操作 (编辑器)
- 深度优先搜索 (DFS)
"""

QUEUE_CONTENT = """
## 队列 (Queue)

### 核心特性
**FIFO (First In First Out)** - 先进先出

### 形象理解
像排队买票，先来的人先买到票。

### 基本操作
- `enqueue(x)` - 入队，将元素放到队尾
- `dequeue()` - 出队，移除队首元素并返回
- `front()` - 查看队首元素
- `is_empty()` - 判断队列是否为空

### Python 实现
```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items.popleft()

    def front(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
```

### 应用场景
- 任务调度 (打印队列)
- 广度优先搜索 (BFS)
- 消息队列
- 滑动窗口问题
"""

PRACTICE = """
## 练习题

### 练习 1: 括号匹配
```python
def is_valid_parentheses(s):
    '''
    判断括号字符串是否有效

    有效示例: "()", "()[]{}", "{[]}"
    无效示例: "(]", "([)]"

    提示: 使用栈，左括号入栈，右括号时检查栈顶是否匹配
    '''
    pass

# 测试
print(is_valid_parentheses("()[]{}"))  # True
print(is_valid_parentheses("([)]"))    # False
```

### 练习 2: 用栈实现队列
```python
class StackQueue:
    '''
    用两个栈实现队列的以下操作:
    - enqueue(x): 入队
    - dequeue(): 出队
    - front(): 查看队首
    - is_empty(): 判断是否为空

    提示: 一个栈负责入队，另一个负责出队
    '''
    def __init__(self):
        self.stack_in = []  # 入队用的栈
        self.stack_out = []  # 出队用的栈

    def enqueue(self, x):
        pass

    def dequeue(self):
        pass

    def front(self):
        pass

    def is_empty(self):
        pass
```

### 思考题
1. 如何用队列实现栈？
2. 浏览器的前进/后退功能用什么数据结构实现？
"""


def get_data():
    return {
        "theory": [STACK_CONTENT, QUEUE_CONTENT],
        "practice": PRACTICE,
        "sample_code": "class Stack: ..."
    }
