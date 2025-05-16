{
    "code": "def linear_time_9(text):\n    count = {}\n    for char in text:\n        if char in count:\n            count[char] += 1\n        else:\n            count[char] = 1\n    return count",
    "complexity": "O(n)"
}