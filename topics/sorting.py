"""
排序算法知识点
"""

BUBBLE_SORT = """
## 冒泡排序 (Bubble Sort)

### 核心思想
重复遍历数组，比较相邻元素并交换位置，使得最大/最小的元素逐渐"浮"到序列末端。

### 算法步骤
1. 从第一个元素开始，比较相邻的两个元素
2. 如果前者大于后者，则交换位置
3. 移动到下一个位置，重复步骤1-2
4. 每轮遍历后，未排序区域的最后一个元素就是最大/最小的

### 时间复杂度
- 平均: O(n²)
- 最好: O(n)（已排序时）
- 最坏: O(n²)

### Python 实现
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # 已经有序，提前结束
            break
    return arr
```

### 图解示意
初始: [5, 2, 8, 1, 9]
第1轮: [2, 5, 8, 1, 9] → [2, 5, 8, 1, 9] → [2, 5, 1, 8, 9] → [2, 5, 1, 8, 9]
第2轮: [2, 1, 5, 8, 9] → [2, 1, 5, 8, 9] → [2, 1, 5, 8, 9]
...
"""

QUICK_SORT = """
## 快速排序 (Quick Sort)

### 核心思想
选择基准元素，将数组分为两部分：小于基准的放左边，大于基准的放右边，然后递归处理。

### 算法步骤
1. 选择一个基准元素（通常选第一个或最后一个）
2. 将数组分为两部分：小元素在左，大元素在右
3. 对左右两部分递归执行快速排序

### 时间复杂度
- 平均: O(n log n)
- 最坏: O(n²)（极度不均衡分割时）

### Python 实现
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

### 与冒泡排序对比
| 特性       | 冒泡排序     | 快速排序        |
|-----------|------------|----------------|
| 时间复杂度  | O(n²)       | O(n log n)     |
| 空间复杂度  | O(1)        | O(log n)       |
| 稳定性     | 稳定         | 不稳定          |
"""

PRACTICE = """
## 练习题

### 练习 1: 选择排序
选择排序的核心是：每轮从未排序部分找出最小元素，放到已排序部分末尾。

请补全下面的代码：
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        # TODO: 在 arr[i+1:] 中找到最小元素的索引
        # 提示: 使用 min() 函数或手动比较
        min_idx = # 你的代码

        # 交换
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

运行测试:
```bash
python -c "from sorting import test_selection; test_selection()"
```

### 练习 2: 验证排序正确性
写一个函数验证数组是否已排序：
```python
def is_sorted(arr):
    # 如果数组长度 <= 1，一定是有序的
    # 否则检查所有相邻对是否满足 arr[i] <= arr[i+1]
    pass

# 测试
print(is_sorted([1, 2, 3, 4, 5]))  # 应输出 True
print(is_sorted([1, 3, 2, 4, 5]))  # 应输出 False
```
"""


def get_data():
    return {
        "theory": [BUBBLE_SORT, QUICK_SORT],
        "practice": PRACTICE,
        "sample_code": "def bubble_sort(arr): ..."
    }
