{
    "code": "def linear_time_6(items):\n    count = 0\n    for i in range(len(items)):\n        if items[i] % 2 == 0:\n            count += 1\n    return count",
    "complexity": "O(n)"
}