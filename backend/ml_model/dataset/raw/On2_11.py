{
    "code": "def quadratic_time_11(nums):\n    n = len(nums)\n    prefix_sums = [0] * (n + 1)\n    for i in range(n):\n        prefix_sums[i + 1] = prefix_sums[i] + nums[i]\n    \n    result = []\n    for i in range(n):\n        for j in range(i, n):\n            subarray_sum = prefix_sums[j + 1] - prefix_sums[i]\n            result.append(subarray_sum)\n    \n    return result",
    "complexity": "O(n^2)"
}