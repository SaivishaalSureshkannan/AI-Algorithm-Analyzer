{
    "code": "def constant_time_6(nums):\n    count = 0\n    for i in range(10):\n        count += i\n    return count + len(nums)",
    "complexity": "O(1)"
}