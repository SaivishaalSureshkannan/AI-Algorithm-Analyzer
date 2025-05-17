{
    "code": "def constant_time_27(cached_data, ttl_seconds, current_time, key):\n    if key in cached_data:\n        entry_time, value = cached_data[key]\n        if current_time - entry_time < ttl_seconds:\n            return value\n    return None",
    "complexity": "O(1)"
}