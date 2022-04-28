from utils import *


class Solution:
    def __init__(self, solution, city):
        self.solution = solution
        m, h, b, c = data(solution, city)
        self.profitability = m
        self.happines = h
        self.num_of_buildings = b
        self.cost = c


def initial_solutions(graph) -> list[Solution]:
    '''generuje początkową populację'''
    pass


def generate_solution(old_solution):
    '''generuje nowe rozwiązanie na podstawie dostarczonego'''
    pass


def first_bees(graph=None, iterations=100, elite_places=3, good_places=2, elite_bees=50, good_bees=25):
    current_solutions = initial_solutions(graph) #lista Solutions - czyli rozwiązanie i obliczona dla niego funkcja celu, posortowane malejąco
    counter = 0

    while counter < iterations:
        chosen_solutions = current_solutions[:elite_places+good_places] #rozwiązania elitarne + dobre
        new_solutions = []

        for i, chosen_solution in enumerate(chosen_solutions):
            local_solutions = []
            for _ in range(elite_bees if i < elite_places else good_bees):
                new_solution = generate_solution(chosen_solution)
                solution = Solution(new_solution, graph)
                local_solutions.append(solution)
            
            local_solutions.sort(lambda el: el.profitability, reverse=True)
            new_solutions.append(local_solutions)
        
        current_solutions = [el[0] for el in new_solutions] #pierwszy krok pętli przerzucony na koniec dla uproszczenia zapisu
        counter+=1
    return chosen_solutions[0]


if __name__ == "__main__":
    pass
