{
    "code": "def exponential_time_2(arr, i=0, subset=[]):\n    if i == len(arr):\n        return [subset]\n    include = exponential_time_2(arr, i+1, subset + [arr[i]])\n    exclude = exponential_time_2(arr, i+1, subset)\n    return include + exclude",
    "complexity": "O(2^n)"
}