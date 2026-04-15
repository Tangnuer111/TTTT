"""
链表基础知识
"""

CONTENT = """
## 链表 (Linked List)

### 核心思想
链表是一种线性数据结构，每个节点包含数据和指向下一个节点的指针，通过指针串联起所有节点。

### vs 数组
| 特性       | 数组          | 链表          |
|-----------|--------------|--------------|
| 存储方式    | 连续内存      | 分散内存       |
| 访问方式    | 随机访问 O(1)  | 顺序访问 O(n)  |
| 插入/删除   | O(n)         | O(1)         |
| 空间开销    | 小           | 大（需存指针）  |

### Python 实现
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 创建链表: 1 -> 2 -> 3 -> 4 -> 5
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# 遍历链表
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\\n")
        current = current.next
```

### 常用操作

#### 1. 反转链表
```python
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_temp = current.next  # 保存下一个节点
        current.next = prev        # 反转指针
        prev = current             # prev 前进
        current = next_temp        # current 前进
    return prev  # 新的头节点
```

#### 2. 合并两个有序链表
```python
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 or l2
    return dummy.next
```

### 图解: 反转链表
```
初始: 1 -> 2 -> 3 -> 4 -> 5 -> None
      ↑
     prev=None, current=1

第1步: 1 -> None, 2 -> 3 -> 4 -> 5 -> None
             ↑
            prev=1, current=2

第2步: 1 <- 2, 3 -> 4 -> 5 -> None
                  ↑
                 prev=2, current=3
...
最终: None <- 1 <- 2 <- 3 <- 4 <- 5
                                  ↑
                                 prev=5 (新头)
```

### LeetCode 经典题目
- 206. 反转链表
- 21. 合并两个有序链表
- 876. 链表的中间节点
- 19. 删除链表的倒数第 N 个节点
"""

PRACTICE = """
## 练习题

### 练习 1: 链表长度
```python
def get_length(head):
    '''返回链表的长度'''
    pass

# 测试
# 创建 1->2->3 的链表并测试
head = create_linked_list([1, 2, 3])
print(get_length(head))  # 应输出 3
```

### 练习 2: 删除节点
```python
def delete_node(head, val):
    '''
    删除链表中第一个值为 val 的节点
    返回新的头节点

    提示: 需要处理头节点是要删除的节点的情况
    '''
    pass
```

### 练习 3: 判断回文链表 (进阶)
```python
def is_palindrome(head):
    '''
    判断链表是否为回文链表

    示例:
    1->2->2->1  是回文 -> True
    1->2->3    不是回文 -> False

    进阶要求: O(n) 时间复杂度和 O(1) 空间复杂度
    提示: 可以用快慢指针找到中点，然后反转后半部分比较
    '''
    pass
```
"""


def get_data():
    return {
        "theory": [CONTENT],
        "practice": PRACTICE,
        "sample_code": "class ListNode: ..."
    }
