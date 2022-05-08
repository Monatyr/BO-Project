import copy

from function import *
from population import *
from load import *


def cross(population, children=100, graph=None):
    for _ in range(children):
        pop = random.choice(population)
        population.append(copy.deepcopy(pop))


def mutate(population, chance=0.1):
    for i in range(len(population)):
        for j in range(len(population[i])):
            if population[i][j] in [1, 2, 3]:
                if random.uniform(0.0, 1.0) <= chance:
                    population[i][j] = random.randint(1, 3)


def select(population, graph, size=100):
    population.sort(key=lambda vector: f(*data(vector, graph)), reverse=True)
    for _ in range(size):
        population.pop()


def evolve(graph, length, epoch=10, size=100, children=100):
    population = get_population(length, size)
    for _ in range(epoch):
        cross(population, children=children)
        mutate(population, chance=0.9)
        select(population, graph, size=size)
    return population[0], f(*data(population[0], graph))


#print(evolve(*get_graph("../../graph/e5"), 1, 2, 2))
print(evolve(city_kos, 12))

"""
    for vector in vectors:
        population.append((vector, f(*data(vector, graph))))
    for _ in range(epoch):
        new_population = copy.deepcopy(population)
        for _ in range(children):
            pop = random.choice(population)[0]
            new_population.append((mutate(pop), f(*data(pop, graph))))
        new_population.sort(key=lambda x: x[1], reverse=True)
        population = new_population[:size]
"""