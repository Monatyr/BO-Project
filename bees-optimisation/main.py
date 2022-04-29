from bees_utils import *


class Solution:
    def __init__(self, solution, city):
        self.solution = solution
        m, h, b, c = data(solution, city)
        self.profitability = m
        self.happines = h
        self.num_of_buildings = b
        self.cost = c


def initial_solutions(graph, num_of_solutions: int, solution_length: int, max_buildings=-1, max_cost=-1) -> list[Solution]:
    '''generuje początkowe populacje i zwraca je posortowane malejąco według ich opłacalności'''
    result = list()
    solutions = get_population(solution_length, num_of_solutions, max_buildings, graph, max_cost)
    for solution in solutions:
        result.append(Solution(solution, graph))
    result.sort(key=lambda el: el.profitability, reverse=True)
    return result


def generate_solution(old_solution, num_of_changes=5):
    '''generuje nowe rozwiązanie na podstawie dostarczonego'''
    new_solution = old_solution.copy()
    edited_nodes = [False for _ in range(len(old_solution))]
    for _ in range(num_of_changes):
        prob = random.random()
        if 0 <= prob < 1:     #zmiana istniejącego budynku
            index = random.randint(1, len(old_solution)-1)
            new_building = random.randint(1, 3)
            new_solution[index] = new_building
        else:                 #dodanie nowego budynku
            pass
    return new_solution
    # pass


def first_bees(graph,  num_of_vertices, iterations=100, elite_places=3, good_places=2, elite_bees=50, good_bees=25) -> Solution:
    current_solutions = initial_solutions(graph, elite_places+good_places, num_of_vertices) #lista Solutions - czyli rozwiązanie i obliczona dla niego funkcja celu, posortowane malejąco
    counter = 0

    while counter < iterations:
        chosen_solutions = current_solutions[:elite_places+good_places] #rozwiązania elitarne + dobre
        new_solutions = []

        for i, chosen_solution in enumerate(chosen_solutions):
            local_solutions = []
            for _ in range(elite_bees if i < elite_places else good_bees):
                new_solution = generate_solution(chosen_solution.solution)
                solution = Solution(new_solution, graph)
                local_solutions.append(solution)
            
            local_solutions.sort(key=lambda el: el.profitability, reverse=True)
            new_solutions.append(local_solutions)
        
        current_solutions = [el[0] for el in new_solutions] #pierwszy krok pętli przerzucony na koniec dla uproszczenia zapisu
        counter+=1
    return chosen_solutions[0]


if __name__ == "__main__":
    G, number_of_vertices = get_graph_edges("graphs/city_kos.txt")
    print(first_bees(G, number_of_vertices).profitability)
