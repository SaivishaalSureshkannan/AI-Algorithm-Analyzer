{
    "code": "def constant_time_14(queue):\n    if len(queue) <= 3:\n        return sum(queue)\n    else:\n        return queue[0] + queue[1] + queue[2]",
    "complexity": "O(1)"
}