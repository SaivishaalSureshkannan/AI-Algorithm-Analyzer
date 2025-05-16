{
    "code": "def linear_time_16(array):\n    seen = set()\n    for element in array:\n        if element in seen:\n            return element\n        seen.add(element)\n    return None",
    "complexity": "O(n)"
}