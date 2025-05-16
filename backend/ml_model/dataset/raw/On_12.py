{
    "code": "def linear_time_12(stream):\n    running_sum = 0\n    counter = 0\n    for value in stream:\n        running_sum += value\n        counter += 1\n    return running_sum / counter if counter > 0 else 0",
    "complexity": "O(n)"
}