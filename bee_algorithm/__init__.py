from .utils import *


max_buildings = -1
max_cost = -1

ADD_THRESHOLD = 0.33
DELETE_THRESHOLD = 0.66

TOP_SOLUTIONS_NUM = 10


class Solution:
    def __init__(self, solution, city):
        self.solution = solution
        m, h, b, c = data(solution, city)
        self.profitability = m
        self.happines = h
        self.num_of_buildings = b
        self.cost = c
        self.counter = 0

    def __lt__(self, other):
        return self.profitability < other.profitability


def initial_solutions(graph, num_of_solutions: int, solution_length: int, max_buildings_param=-1, max_cost_param=-1):
    """
    generuje początkowe populacje i zwraca je posortowane malejąco według ich opłacalności
    """

    global max_buildings, max_cost
    max_buildings, max_cost = max_buildings_param, max_cost_param
    result = list()
    solutions = get_population(solution_length, num_of_solutions, max_buildings, graph, max_cost)
    for solution in solutions:
        result.append(Solution(solution, graph))
    result.sort(key=lambda el: el.profitability, reverse=True)
    return result


def check_building_num(solution):
    global max_buildings
    if max_buildings == -1:
        return True
    counter = 0
    for i in range(1, len(solution) - 1):
        if solution[i] != -1:
            counter += 1
            if counter > max_buildings:
                return False
    return True


def check_cost(solution):
    global max_cost
    if max_cost == -1:
        return True
    cost = 0
    for i in range(1, len(solution) - 1):
        cost += COSTS[solution[i]]
        if cost > max_cost:
            return False
    return True


def check_constraints(solution, index):
    new_solution = solution.copy()
    for i in [1, 2, 3]:
        new_solution[index] = i
        if check_cost(new_solution) and check_building_num(new_solution):
            return True
    return False


def count_empty(solution):
    counter = 0
    for building in solution:
        if building == NOTHING:
            counter += 1
    return counter


def count_empty_unchanged(solution, edited_nodes):
    counter = 0
    for i in range(len(solution)):
        if solution[i] == NOTHING and not edited_nodes[i]:
            counter += 1
    return counter


def get_empty_unchanged_index(solution, edited_nodes):
    nodes = []
    for i in range(1, len(solution)):
        if solution[i] == NOTHING and not edited_nodes[i]:
            nodes.append(i)
    return nodes


def generate_solution(old_solution, G, num_of_changes=5):
    """
    generuje nowe rozwiązanie na podstawie dostarczonego
    """

    global max_buildings, max_cost
    new_solution = old_solution.copy()
    edited_nodes = [False for _ in range(len(old_solution))]
    changes_counter = 0
    empty_counter = count_empty(old_solution)
    while changes_counter < num_of_changes:
        prob = random.random()
        loop_counter = 0
        if 0 <= prob < ADD_THRESHOLD:  # zmiana istniejącego budynku
            # print("CHUNG")
            while True:
                loop_counter += 1
                if loop_counter > len(old_solution):
                    break
                index = random.randint(1, len(old_solution) - 1)
                if not edited_nodes[index] and new_solution[index] != -1:
                    while True:
                        new_building = random.randint(1, 3)
                        temp_solution = new_solution.copy()
                        temp_solution[index] = new_building
                        if check_cost(temp_solution):  # liczba budynków się nie zmienia, więc sprawdzamy sam koszt
                            if new_building != new_solution[index]:
                                changes_counter += 1
                                edited_nodes[index] = True
                            new_solution[index] = new_building
                            break
                    break
        elif ADD_THRESHOLD <= prob < DELETE_THRESHOLD and empty_counter > 0:  # dodanie nowego budynku
            # print("ADDUM")
            available_nodes = get_empty_unchanged_index(new_solution, edited_nodes)
            while True:
                loop_counter += 1
                if loop_counter > len(old_solution):
                    break
                if not available_nodes:
                    break
                index = random.choice(available_nodes)

                if not check_constraints(new_solution, index):
                    break

                connected = False
                for e in G:  # sprawdź czy wylosowany wierzchołek jest połączony z innym budynkiem
                    if index in e:
                        adjacent = e[int(not e.index(index))]  # znajdź drugi wierzchołek na krawędzi
                        if new_solution[adjacent] != -1:
                            connected = True
                            break
                if not connected:
                    continue

                # print(f'node was edited = {edited_nodes[index]}\nprevious value = {new_solution[index]}\n\n')
                # print(f'empty_counter = {empty_counter}\nreal count = {count_empty_unchanged(new_solution, edited_nodes)}\n\n')
                if not edited_nodes[index] and new_solution[index] == -1:
                    while True:
                        new_building = random.randint(1, 3)
                        temp_solution = new_solution.copy()
                        temp_solution[index] = new_building
                        if check_cost(temp_solution) and check_building_num(temp_solution):
                            new_solution[index] = new_building
                            edited_nodes[index] = True
                            changes_counter += 1
                            empty_counter -= 1
                            break
                    break
        elif DELETE_THRESHOLD <= prob <= 1:  # usunięcie budynku
            # print("DELET")
            while True:
                loop_counter += 1
                if loop_counter > len(old_solution):
                    break

                index = random.randint(1, len(old_solution) - 1)
                connected = True
                temp_solution = new_solution.copy()
                temp_solution[index] = -1
                for e in G:  # sprawdź czy po usunięciu wierzchołka jeden z jego sąsiadów-budynków nie zostanie odłączony od reszty
                    if index in e:
                        adjacent = e[int(not e.index(index))]  # znajdź drugi wierzchołek na krawędzi
                        if temp_solution[adjacent] == -1:
                            continue
                        connected_adj = False
                        for e2 in G:
                            if adjacent in e2 and index not in e2:
                                adj_of_adjacent = e2[int(not e2.index(adjacent))]  # znajdź otoczenie sąsiada index-u
                                if temp_solution[adj_of_adjacent] != -1:
                                    connected_adj = True
                                    break
                        if not connected_adj:
                            connected = False
                            break
                if not connected:
                    continue

                if not edited_nodes[index] and new_solution[index] != -1:
                    new_solution[index] = -1
                    edited_nodes[index] = True
                    changes_counter += 1
                    break
    # print(new_solution)
    return new_solution


def update_top(top, solution):
    top.append(solution)
    top.sort(key=lambda el: el.profitability, reverse=True)
    if len(top) >= TOP_SOLUTIONS_NUM:
        top.pop(-1)


def first_bees(graph, num_of_vertices, it=40, ep=3, gp=2, eb=50, gb=25) -> list[Solution]:
    current_solutions = initial_solutions(
        graph,
        ep + gp,
        num_of_vertices
    )  # lista Solutions - czyli rozwiązanie i obliczona dla niego funkcja celu, posortowane malejąco
    counter = 0

    top_solutions = []

    while counter < it:
        chosen_solutions = current_solutions[:ep + gp]  # rozwiązania elitarne + dobre
        new_solutions = []

        for i, chosen_solution in enumerate(chosen_solutions):
            local_solutions = []
            chosen_solution.counter += 1
            for _ in range(eb if i < ep else gb):
                new_solution = generate_solution(chosen_solution.solution, graph)
                solution = Solution(new_solution, graph)
                local_solutions.append(solution)
                update_top(top_solutions, solution)
            local_solutions.sort(key=lambda el: el.profitability, reverse=True)
            new_solutions.append(local_solutions)

        current_solutions = [el[0] for el in
                             new_solutions]  # pierwszy krok pętli przerzucony na koniec dla uproszczenia zapisu
        for sol in current_solutions:
            if sol.counter > 10 and sol in top_solutions:
                current_solutions.remove(sol)
        current_solutions.sort(key=lambda el: el.profitability, reverse=True)
        counter += 1
    return top_solutions
