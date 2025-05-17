{
    "code": "def constant_time_21(circular_buffer, position):\n    buffer_size = len(circular_buffer)\n    return circular_buffer[position % buffer_size]",
    "complexity": "O(1)"
}