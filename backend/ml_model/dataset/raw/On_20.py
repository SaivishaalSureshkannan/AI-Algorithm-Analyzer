{
    "code": "def linear_time_20(s, t):\n    count_s = {}\n    count_t = {}\n    \n    for char in s:\n        count_s[char] = count_s.get(char, 0) + 1\n    \n    for char in t:\n        count_t[char] = count_t.get(char, 0) + 1\n    \n    return count_s == count_t",
    "complexity": "O(n)"
}