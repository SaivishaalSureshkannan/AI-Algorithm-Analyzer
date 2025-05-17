{
    "code": "def constant_time_25(deque_obj):\n    if len(deque_obj) >= 3:\n        front = deque_obj.popleft()\n        back = deque_obj.pop()\n        deque_obj.appendleft(back)\n        deque_obj.append(front)\n    return deque_obj",
    "complexity": "O(1)"
}