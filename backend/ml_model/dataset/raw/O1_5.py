{
    "code": "def constant_time_5(data):\n    if not data:\n        return None\n    first = data[0]\n    last = data[-1]\n    return (first + last) / 2",
    "complexity": "O(1)"
}