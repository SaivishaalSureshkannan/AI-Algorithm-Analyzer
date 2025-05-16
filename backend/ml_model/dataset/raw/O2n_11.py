{
    "code": "def exponential_time_11(nums):\n    def backtrack(start, path):\n        result.append(path[:])\n        for i in range(start, len(nums)):\n            path.append(nums[i])\n            backtrack(i + 1, path)\n            path.pop()\n    \n    result = []\n    backtrack(0, [])\n    return result",
    "complexity": "O(2^n)"
}