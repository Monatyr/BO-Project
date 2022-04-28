'''
UWAGI:

Co należy robić w drugiej pętli?

Q: Wybór m sąsiedztw do przeszukiwania - czy mają to być najlepsze miejsca z poprzedniej iteracji, tzn. elitarne i dobre,
czy raczej wygenerowanie sąsiedztw dla miejsc elitarnych i dobrych?
A: Wydaje mi się, że wybranie topki z poprzedniej iteracji.

Jeśli jest tak jak mi się wydaje, to rekrutuję wtedy dużo pszczół do wszystkich miejsc elitarnych
i mniej do miejsc dobrych.

Uzyskuję w ten sposób dla każdego sąsiedztwa nowy zbiór rozwiązań i liczbę dla wszystkich elementów funkcję celu. Następnie sortuję rozwiązania
względem ich wyniku.

Z każdego batcha wyników dla sąsiedztw wybieram najlepsze lokalne rozwiązanie.
Zbieram najlepsze lokalne wyniki i tworze z nich populację rozwiązań na następną iterację
(o ile są lepsze od starych rozwiązań lub stare rozwiązania się przeterminowały - były za długo już sprawdzane i mogliśmy utknąć w maksimum lokalnym)

Aby zabezpieczyć się przed niebezpieczeństwem utknięcia w maksimum lokalnym, możemy każdemu rozwiązaniu nadać datę ważności. Jeśli dane rozwiązanie
jest zbyt długo rozważane, to zapamietujemy je jako jedno z lepszych rozwiązań, ale wyrzucamy je z puli aktywnie rozważanych - dzięki temu nie tracimy
mocy obliczeniowej na potencjalnie bezsensowny task

Problematyczne będzie generowanie nowych rozwiązań - jak to robić?
'''


'''
POMYSŁ NA FUNCKJĘ GENERUJĄCĄ NOWE ROZWIĄZANIE:

Mieć 3 operacje - usunięcie, dodanie i zmiana budynku
Będziemy mieli określoną liczbę dostępnych zmian w rozwiązaniu.
Zbiór naszych zmian będziemy losować - najpierw typ operacji, a następnie miejsce, gdzie ma to zajść
Każda operacja będzie miała swoje prawdopodobieństwo wylosowania (usunięcie najniższe).
Operacja usunięcia będzie miała pierwszeństwo przed wszystkimi innymi, ponieważ obniża ona koszt miasta
oraz liczbę budynków, co zwiększa sznase na wykonanie następnych operacji w kolejce.
Jeśli zabraknie nam środków lub miejsca na wykonanie operacji, to po prostu jej nie wykonujemy.

Być może całkowicie powinno się zrezygnować z usuwania budynków - ułatwiłoby to zachowanie spójności grafu rozwiązania.
Niestety uniemożliwiłoby to zmianę kształtu miasta. Jeśli zostawimy możliwość usuwania budynków, to za każdym wykonaniem
tej operacji powinniśmy upewnić się, że graf pozostaje spójny.
'''


'''
WSTĘPNY POMYSŁ:

Liczba iteracji = 100
Miejsca elitarne = 3
Miejsca dobre = 2
Elitarne pszczoły = 50
Dobre pszczoły = 25    ///dzięki temu uzyskujemy 2*25 + 3*50 = 200 rozwiązań

'''

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
