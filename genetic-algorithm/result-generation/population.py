import numpy as np
import random
from consts import *


def get_population(length, size, graph=None, max_buildings=None, max_cost=None):
    population = []
    # case 1
    if max_buildings is None and max_cost is None:
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
            if max_cost is None:
                for _ in range(max_buildings):
                    vertex = random.choice(list(vertices_possible - vertices_done))
                    vector[vertex] = random.choice([HOUSE, FUN, WORK])
                    for (u, v) in graph:
                        if vertex in (u, v):
                            vertices_possible.add(v)
                            vertices_possible.add(u)
                    vertices_done.add(vertex)
            # case 3
            elif max_buildings is None:
                cost = 0
                while True:
                    vertex = random.choice(list(vertices_possible - vertices_done))
                    choice = random.choice([HOUSE, FUN, WORK])
                    if cost + COSTS[choice] > max_cost:
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
                    if cost + COSTS[choice] > max_cost or buildings + 1 > max_buildings:
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