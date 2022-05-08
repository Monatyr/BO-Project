import random


def get_graph(file):
    f = open(file, "r")
    lines = f.readlines()
    graph = []
    for l in lines:
        s = l.split()
        if s[0] == "p":
            length = int(s[2])
        if s[0] == "e":
            graph.append((int(s[1])-1, int(s[2])-1))

    vertices_possible = set()
    vertices_done = set()
    vertices_possible.add(0)
    while vertices_possible - vertices_done:
        vertex = random.choice(list(vertices_possible - vertices_done))
        for (u, v) in graph:
            if vertex in (u, v):
                vertices_possible.add(v)
                vertices_possible.add(u)
        vertices_done.add(vertex)

    if len(vertices_possible) != length:
        raise Exception("The graph is not connected")

    return (graph, length)