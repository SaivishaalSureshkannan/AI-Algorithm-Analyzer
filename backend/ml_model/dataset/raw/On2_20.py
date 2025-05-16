{
    "code": "def quadratic_time_20(nums):\n    subarrays = []\n    for i in range(len(nums)):\n        current_sum = 0\n        for j in range(i, len(nums)):\n            current_sum += nums[j]\n            subarrays.append((i, j, current_sum))\n    \n    # Sort subarrays by sum\n    subarrays.sort(key=lambda x: x[2])\n    return subarrays",
    "complexity": "O(n^2)"
}