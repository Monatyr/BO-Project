import random
from queue import Queue
from utils.const_values import *
from utils.population import get_population


def data(solution, city):
    money = 0
    happiness = 0
    cost = 0
    buildings = 0
    for building in solution:
        if building == NOTHING:
            pass
        elif building == CENTRE:
            pass
        elif building == HOUSE:
            cost += HOUSE_COST
            buildings += 1
        elif building == FUN:
            happiness += 1
            cost += FUN_COST
            buildings += 1
        elif building == WORK:
            happiness -= 1
            cost += WORK_COST
            buildings += 1
        else:
            print("Wrong building!")

    for (x, y) in city:
        (m, h) = value[(solution[x], solution[y])]
        money += m
        happiness += h

    if happiness < -5:
        happiness = -5
    elif happiness > 5:
        happiness = 5

    return money, happiness, buildings, cost


def f(money, happiness):
    if happiness < 0:
        real_money = (1 + HAPPINESS_TIME * happiness) * money - HAPPINESS_TIME * happiness * money / 2
    elif happiness > 0:
        real_money = (1 - HAPPINESS_TIME * happiness) * money + HAPPINESS_TIME * happiness * money * 2
    else:
        real_money = money
    return real_money


def get_graph_edges(file):
    f = open(file, "r")
    lines = f.readlines()
    graph = []
    for line in lines:
        s = line.split()
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

    return graph, length


class Node():
    def __init__(self, i):
        self.neighbours = list()
        self.visited = False
        self.index = i


def get_graph(filename: str):
    graph = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        graph = [Node(i) for i in range(int(lines[0].split()[2]))]
        for line in lines[1:]:
            u, v = line.split()[1:]
            u, v = int(u), int(v)
            graph[u-1].neighbours.append(graph[v-1])
            graph[v-1].neighbours.append(graph[u-1])
    return graph


def check_connectivity(graph):
    q = Queue()
    q.put(graph[0])
    visited = 0

    for node in graph:
        node.visited = False

    while not q.empty():
        u = q.get()
        u.visited = True
        visited += 1

        for n in u.neighbours:
            if not n.visited:
                q.put(n)
                n.visited = True

    return visited == len(graph)


if __name__ == "__main__":
    G = get_graph('graphs/graph')
    print(check_connectivity(G))
    # pop_graph = get_graph_edges('graphs/graph')[0]
    # get_population(5, 1, max_buildings=5, graph=pop_graph, max_cost=100000000)

    G, number_of_vertices = get_graph_edges('graphs/graph')
    print(get_population(number_of_vertices, 5, max_buildings=number_of_vertices, max_cost=60000, graph=G))
