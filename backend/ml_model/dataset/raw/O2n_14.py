{
    "code": "def exponential_time_14(graph, start):\n    def dfs(node, visited):\n        visited.add(node)\n        paths = [[node]]\n        \n        for neighbor in graph.get(node, []):\n            if neighbor not in visited:\n                for path in dfs(neighbor, visited.copy()):\n                    paths.append([node] + path)\n        \n        return paths\n    \n    return dfs(start, set())",
    "complexity": "O(2^n)"
}