"""
二分查找知识点
"""

CONTENT = """
## 二分查找 (Binary Search)

### 核心思想
在有序数组中，通过每次将搜索范围缩小一半来快速定位目标元素。

### 算法前提
数组必须有序！

### 算法步骤
1. 设置左右边界 (left, right)
2. 计算中点 mid = (left + right) // 2
3. 比较 arr[mid] 与目标值:
   - 相等: 找到目标，返回索引
   - arr[mid] < 目标: 目标在右半部分，left = mid + 1
   - arr[mid] > 目标: 目标在左半部分，right = mid - 1
4. 重复步骤 2-3，直到找到目标或 left > right

### 时间复杂度
- O(log n) - 每次排除一半元素

### Python 实现 (递归版)
```python
def binary_search_recursive(arr, target, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1  # 未找到

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
```

### Python 实现 (循环版)
```python
def binary_search_loop(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # 未找到
```

### 图解示意
在有序数组 [1, 3, 5, 7, 9, 11, 13] 中查找 7:

```
第1轮: left=0, right=6, mid=3
       [1, 3, 5, 7, 9, 11, 13]
                ↑
       arr[3]=7 = 目标! 找到!

查找 6:
第1轮: left=0, right=6, mid=3 → arr[3]=7 > 6, right=2
第2轮: left=0, right=2, mid=1 → arr[1]=3 < 6, left=2
第3轮: left=2, right=2, mid=2 → arr[2]=5 < 6, left=3
left > right, 返回 -1 (未找到)
```

### 应用场景
- 在有序数据中查找
- 求第一个/最后一个满足条件的元素
- 优化 O(n) 的线性查找
- 在题解中常用于"在 ... 中查找"类的题目
"""

PRACTICE = """
## 练习题

### 练习 1: 实现循环版二分查找
```python
def binary_search(arr, target):
    # 使用循环实现
    # 返回目标索引，如果不存在返回 -1
    pass

# 测试
arr = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(arr, 7))   # 应输出 3
print(binary_search(arr, 6))   # 应输出 -1
```

### 练习 2: 查找第一个大于目标的值
```python
def find_first_greater(arr, target):
    '''
    在有序数组中，找到第一个大于 target 的元素的索引
    如果不存在，返回 -1

    示例:
    arr = [1, 3, 5, 7, 9]
    find_first_greater(arr, 4) -> 2  (因为 arr[2]=5 是第一个 > 4 的)
    find_first_greater(arr, 9) -> -1
    '''
    pass
```

### 思考题
如果要在 10000 个有序元素中查找，二分查找最多需要比较多少次？
提示: log₂(10000) ≈ ?
"""


def get_data():
    return {
        "theory": [CONTENT],
        "practice": PRACTICE,
        "sample_code": "def binary_search(arr, target): ..."
    }
