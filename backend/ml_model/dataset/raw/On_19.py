{
    "code": "def linear_time_19(nums, target):\n    # Linear search implementation: O(n)\n    for i in range(len(nums)):\n        if nums[i] == target:\n            return i\n    return -1",
    "complexity": "O(n)"
}