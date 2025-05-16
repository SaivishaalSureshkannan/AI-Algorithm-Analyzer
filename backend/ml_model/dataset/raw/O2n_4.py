{
    "code": "def exponential_time_4(n):\n    if n == 0:\n        return 1\n    count = 0\n    for i in range(n):\n        count += exponential_time_4(n-1)\n    return count",
    "complexity": "O(2^n)"
}