def get_dimacs(graph):
    size = 0
    for (u, v) in graph:
        size = max(size, u, v)
    dimacs = [set() for _ in range(size+1)]
    for (u, v) in graph:
        dimacs[u].add(v)
        dimacs[v].add(u)
    return dimacs
