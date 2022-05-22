import copy
import random

from utils.population import get_population
from utils.adaptation import *


def cross(population, children=100, graph=None, max_buildings=None, max_cost=None):
    for _ in range(children):
        parent1 = random.choice(population)
        parent2 = random.choice(population)
        child = [NOTHING for _ in range(len(parent1))]
        child[0] = CENTRE
        vertices_merged = set()
        vertices_merged.add(0)
        for i in range(len(parent1)):
            if parent1[i] in [HOUSE, FUN, WORK]:
                vertices_merged.add(i)
        for i in range(len(parent2)):
            if parent2[i] in [HOUSE, FUN, WORK]:
                vertices_merged.add(i)
        vertices_possible = set()
        vertices_done = set()
        vertices_possible.add(0)
        n = -1
        c = 0
        while vertices_merged - vertices_done:
            vertex = random.choice(list((vertices_merged & vertices_possible) - vertices_done))
            building = NOTHING
            while building == NOTHING:
                building = random.choice([parent1[vertex], parent2[vertex]])
            if max_cost is not None and c+COSTS[building] > max_cost:
                break
            c += COSTS[building]
            n += 1
            child[vertex] = building
            for (u, v) in graph:
                if vertex in (u, v):
                    vertices_possible.add(v)
                    vertices_possible.add(u)
            vertices_done.add(vertex)
            if max_buildings is not None and n == max_buildings:
                break
        while vertices_possible - vertices_done:
            if max_buildings is not None and n == max_buildings:
                break
            vertex = random.choice(list(vertices_possible - vertices_done))
            building = random.choice([HOUSE, FUN, WORK])
            if max_cost is not None and c+COSTS[building] > max_cost:
                break
            c += COSTS[building]
            n += 1
            child[vertex] = building
        population.append(copy.deepcopy(child))


def mutate(population, chance=0.1, max_cost=None):
    for i in range(1, len(population)):
        c = cost(population[i])
        for j in range(len(population[i])):
            if population[i][j] in [HOUSE, FUN, WORK]:
                if random.uniform(0.0, 1.0) <= chance:
                    now = population[i][j]
                    building = random.choice([HOUSE, FUN, WORK])
                    if max_cost is not None and c+COSTS[building]-COSTS[now] <= max_cost:
                        population[i][j] = building
                        c += COSTS[building]-COSTS[now]
                    else:
                        population[i][j] = building


def select(population, graph, size=100):
    population.sort(key=lambda vector: f(*data(vector, graph)), reverse=True)
    while len(population) != size:
        population.pop()


def evolve(graph, length, epoch=100, size=100, children=100, chance=0.1, maxb=None, maxc=None):
    population = get_population(length, size, graph=graph, max_buildings=maxb, max_cost=maxc)
    print("{:.2f}%".format(0), data(population[0], graph), "==", f(*data(population[0], graph)), "with", str(cost(population[0]))+"$", buildings(population[0]))
    for percent in range(epoch):
        cross(population, children=children, graph=graph, max_buildings=maxb, max_cost=maxc)
        mutate(population, chance=chance, max_cost=maxc)
        select(population, graph, size=size)
        print("{:.2f}%".format(100*(percent+1)/epoch), data(population[0], graph), "==", f(*data(population[0], graph)), str(cost(population[0]))+"$", buildings(population[0]))
    return population[0], f(*data(population[0], graph))
