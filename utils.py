import random
import numpy as np

NOTHING = -1
CENTRE = 0
HOUSE = 1
FUN = 2
WORK = 3

HAPPINESS_TIME = 0.1  # [0, 0.2]

HOUSE_COST = 25600
FUN_COST = 12800
WORK_COST = 19200
COSTS = [0, HOUSE_COST, FUN_COST, WORK_COST]

value = {}

value[(NOTHING, NOTHING)] = (0, 0)
value[(NOTHING, CENTRE)] = (0, 0)
value[(NOTHING, HOUSE)] = (0, 0)
value[(NOTHING, FUN)] = (0, 0)
value[(NOTHING, WORK)] = (0, 0)

value[(CENTRE, NOTHING)] = (0, 0)
value[(CENTRE, CENTRE)] = (0, 0)
value[(CENTRE, HOUSE)] = (0, 0)
value[(CENTRE, FUN)] = (0, 1)
value[(CENTRE, WORK)] = (1, 0)

value[(HOUSE, NOTHING)] = (0, 0)
value[(HOUSE, CENTRE)] = (0, 0)
value[(HOUSE, HOUSE)] = (0, 0)
value[(HOUSE, FUN)] = (0, 1)
value[(HOUSE, WORK)] = (1, 0)

value[(FUN, NOTHING)] = (0, 0)
value[(FUN, CENTRE)] = (0, 1)
value[(FUN, HOUSE)] = (0, 1)
value[(FUN, FUN)] = (0, 0)
value[(FUN, WORK)] = (0, -1)

value[(WORK, NOTHING)] = (0, 0)
value[(WORK, CENTRE)] = (1, 0)
value[(WORK, HOUSE)] = (1, 0)
value[(WORK, FUN)] = (0, -1)
value[(WORK, WORK)] = (0, 0)


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

    return (money, happiness, buildings, cost)


def f(money, happiness, buildings, cost):
    if happiness < 0:
        real_money = (1 + HAPPINESS_TIME * happiness) * money - HAPPINESS_TIME * happiness * money / 2
    elif happiness > 0:
        real_money = (1 - HAPPINESS_TIME * happiness) * money + HAPPINESS_TIME * happiness * money * 2
    else:
        real_money = money
    return real_money


def get_population(length, size, max_buildings=-1, graph=None, max_cost=-1):
    population = []
    # case 1 - no limits
    if max_buildings == -1 and max_cost == -1:
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
            # case 2 - no max cost
            if max_cost == -1:
                for _ in range(max_buildings):
                    vertex = random.choice(list(vertices_possible - vertices_done))
                    vector[vertex] = random.choice([HOUSE, FUN, WORK])
                    for (u, v) in graph:
                        if vertex in (u, v):
                            vertices_possible.add(v)
                            vertices_possible.add(u)
                    vertices_done.add(vertex)
            # case 3 - no max buildings
            elif max_buildings == -1:
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
            # case 4 - all restraints active
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

    return graph, length