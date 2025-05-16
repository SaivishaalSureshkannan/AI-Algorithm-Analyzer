{
    "code": "def exponential_time_13(n, k):\n    def generate_combinations(nums, k, start, path, result):\n        if len(path) == k:\n            result.append(path[:])\n            return\n        \n        for i in range(start, len(nums)):\n            path.append(nums[i])\n            generate_combinations(nums, k, i + 1, path, result)\n            path.pop()\n    \n    nums = list(range(1, n + 1))\n    result = []\n    generate_combinations(nums, k, 0, [], result)\n    return result",
    "complexity": "O(2^n)"
}