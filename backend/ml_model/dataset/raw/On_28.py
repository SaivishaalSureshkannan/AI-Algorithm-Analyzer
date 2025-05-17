{
    "code": "def linear_time_28(linked_list_head):\n    # Find middle node of a linked list using two pointers\n    if not linked_list_head:\n        return None\n    slow = fast = linked_list_head\n    while fast and fast.next:\n        slow = slow.next\n        fast = fast.next.next\n    return slow",
    "complexity": "O(n)"
}