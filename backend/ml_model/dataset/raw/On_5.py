{
    "code": "def linear_time_5(data):\n    max_val = float('-inf')\n    for num in data:\n        if num > max_val:\n            max_val = num\n    return max_val",
    "complexity": "O(n)"
}