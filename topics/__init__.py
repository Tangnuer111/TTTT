"""
知识点模块
每个知识点包含：名称、描述、理论、示例代码、练习题
"""

TOPICS = [
    {
        "id": "sorting",
        "name": "排序算法",
        "icon": "📊",
        "desc": "学习冒泡、插入、快排等基础排序算法",
        "module": "sorting"
    },
    {
        "id": "binary_search",
        "name": "二分查找",
        "icon": "🔍",
        "desc": "掌握有序数组的高效搜索方法",
        "module": "binary_search"
    },
    {
        "id": "linked_list",
        "name": "链表基础",
        "icon": "🔗",
        "desc": "理解单链表的操作与应用场景",
        "module": "linked_list"
    },
    {
        "id": "stack_queue",
        "name": "栈与队列",
        "icon": "📦",
        "desc": "两种重要的线性数据结构",
        "module": "stack_queue"
    },
]


def get_topic_data(topic_id: str) -> dict:
    """动态加载知识点数据"""
    if topic_id == "sorting":
        from topics.sorting import get_data
    elif topic_id == "binary_search":
        from topics.binary_search import get_data
    elif topic_id == "linked_list":
        from topics.linked_list import get_data
    elif topic_id == "stack_queue":
        from topics.stack_queue import get_data
    else:
        return {}
    return get_data()
