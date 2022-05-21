import sys
from bee_algorithm import first_bees, get_graph_edges
from gen_algorithm import evolve
from utils.graph import get_graph

ALGO_BEE = 'bee'
ALGO_GEN = 'gen'

if __name__ == '__main__':
    # python main.py [bee|gen]
    if len(sys.argv) < 2:
        print(f'Wrong number of arguments! Use: python main.py [{ALGO_BEE}|{ALGO_GEN}]')
        exit(1)

    ALGO_TYPE = sys.argv[1].lower()
    args = sys.argv[2:]

    d = dict()
    for arg in args:
        res = arg.lower().split('=')
        d[res[0]] = int(res[1])

    # python main.py [bee] [it] [ep] [gp] [eb] [gb]
    if ALGO_TYPE == ALGO_BEE:
        G, number_of_vertices = get_graph_edges("graphs/city_kos")
        solutions = first_bees(G, number_of_vertices, **d)
        for solution in solutions:
            print(f'{solution.solution}   {solution.profitability}')

    # python main.py [gen] [epoch] [size] [children] [maxb] [maxc]
    elif ALGO_TYPE == ALGO_GEN:
        evolve(*get_graph("graphs/f30"), **d)
    else:
        print(f'Wrong argument! Use: python main.py [{ALGO_BEE}|{ALGO_GEN}]')
        exit(1)
