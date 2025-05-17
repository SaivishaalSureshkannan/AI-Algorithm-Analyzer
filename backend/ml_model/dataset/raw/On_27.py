{
    "code": "def linear_time_27(arr):\n    # Kadane's algorithm for maximum subarray sum\n    if not arr:\n        return 0\n    current_max = global_max = arr[0]\n    for i in range(1, len(arr)):\n        current_max = max(arr[i], current_max + arr[i])\n        global_max = max(global_max, current_max)\n    return global_max",
    "complexity": "O(n)"
}