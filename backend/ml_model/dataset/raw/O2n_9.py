{
    "code": "def exponential_time_9(graph, start, end, path=[]):\n    path = path + [start]\n    if start == end:\n        return [path]\n    if start not in graph:\n        return []\n    paths = []\n    for node in graph[start]:\n        if node not in path:\n            new_paths = exponential_time_9(graph, node, end, path)\n            for p in new_paths:\n                paths.append(p)\n    return paths",
    "complexity": "O(2^n)"
}