{
    "code": "def exponential_time_6(nums, target, index=0):\n    if index == len(nums):\n        return 1 if target == 0 else 0\n    include = exponential_time_6(nums, target - nums[index], index + 1)\n    exclude = exponential_time_6(nums, target, index + 1)\n    return include + exclude",
    "complexity": "O(2^n)"
}