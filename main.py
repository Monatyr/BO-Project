import copy
import random
from function import *
from exaples import *
import numpy as np


def get_population(length, size, max_buildings=-1, graph=None, max_cost=-1):
    population = []
    # case 1
    if max_buildings==-1 and max_cost==-1:
        for _ in range(size):
            vector = list(np.random.choice([HOUSE, FUN, WORK], size=length))
            vector[0] = CENTRE
            population.append(vector)
    # case 2,3,4
    else:
        if graph is None:
            raise Exception("No graph!")
        for _ in range(size):
            vector = [NOTHING for _ in range(length)]
            vector[0] = CENTRE
            vertices_possible = set()
            vertices_done = set()
            for (u, v) in graph:
                if 0 in (u, v):
                    vertices_possible.add(v)
                    vertices_possible.add(u)
            vertices_done.add(0)
            # case 2
            if max_cost==-1:
                for _ in range(max_buildings):
                    vertex = random.choice(list(vertices_possible - vertices_done))
                    vector[vertex] = random.choice([HOUSE, FUN, WORK])
                    for (u, v) in graph:
                        if vertex in (u, v):
                            vertices_possible.add(v)
                            vertices_possible.add(u)
                    vertices_done.add(vertex)
            # case 3
            elif max_buildings==-1:
                cost = 0
                while True:
                    vertex = random.choice(list(vertices_possible - vertices_done))
                    choice = random.choice([HOUSE, FUN, WORK])
                    if cost+COSTS[choice] > max_cost:
                        break
                    cost += COSTS[choice]
                    vector[vertex] = choice
                    for (u, v) in graph:
                        if vertex in (u, v):
                            vertices_possible.add(v)
                            vertices_possible.add(u)
                    vertices_done.add(vertex)
            # case 4
            else:
                cost = 0
                buildings = 0
                while True:
                    vertex = random.choice(list(vertices_possible - vertices_done))
                    choice = random.choice([HOUSE, FUN, WORK])
                    if cost+COSTS[choice]>max_cost or buildings+1>max_buildings:
                        break
                    cost += COSTS[choice]
                    buildings += 1
                    vector[vertex] = choice
                    for (u, v) in graph:
                        if vertex in (u, v):
                            vertices_possible.add(v)
                            vertices_possible.add(u)
                    vertices_done.add(vertex)
            population.append(vector)
    return population

"""
def mutate(vector):
    new = []
    for num in vector:
        if num == 0:
            new.append(num)
            continue
        if random.randint(0, 9) == 0:
            new.append(random.randint(1, 3))
        else:
            new.append(num)
    return new


def evolve(graph, length, epoch=10, size=100, children=100):
    vectors = get_population(length, size)
    population = []
    for vector in vectors:
        population.append((vector, f(*data(vector, graph))))
    for _ in range(epoch):
        new_population = copy.deepcopy(population)
        for _ in range(children):
            pop = random.choice(population)[0]
            new_population.append((mutate(pop), f(*data(pop, graph))))
        new_population.sort(key=lambda x: x[1], reverse=True)
        population = new_population[:size]
    return population[0]


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


print(evolve(*get_graph("graph/f30")))
"""