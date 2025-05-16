{
    "code": "def linear_time_14(nums):\n    left_sum = 0\n    total_sum = sum(nums)\n    \n    for i, num in enumerate(nums):\n        total_sum -= num\n        if left_sum == total_sum:\n            return i\n        left_sum += num\n    return -1",
    "complexity": "O(n)"
}