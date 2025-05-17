{
    "code": "def constant_time_24(rgb_color):\n    r, g, b = rgb_color\n    luminance = 0.299 * r + 0.587 * g + 0.114 * b\n    return 'light' if luminance > 128 else 'dark'",
    "complexity": "O(1)"
}