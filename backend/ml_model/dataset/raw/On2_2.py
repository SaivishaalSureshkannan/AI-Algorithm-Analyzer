{
    "code": "def quadratic_time_2(arr):\n    n = len(arr)\n    for i in range(n):\n        for j in range(i+1, n):\n            if arr[i] > arr[j]:\n                arr[i], arr[j] = arr[j], arr[i]\n    return arr",
    "complexity": "O(n^2)"
}