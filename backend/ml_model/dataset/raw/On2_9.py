{
    "code": "def quadratic_time_9(nums):\n    pairs = []\n    for i in range(len(nums)):\n        for j in range(len(nums)):\n            if i != j and nums[i] + nums[j] == 10:\n                pairs.append((nums[i], nums[j]))\n    return pairs",
    "complexity": "O(n^2)"
}