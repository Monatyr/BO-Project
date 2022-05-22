import sys
from bee_algorithm import bees_optimization_algorithm, get_graph_edges
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
    FILE_NAME = "city_kos"
    args = sys.argv[2:]

    d = dict()
    for arg in args:
        res = arg.lower().split('=')
        if res[0] != 'fn':
            res[1] = int(res[1])
        d[res[0]] = res[1]

    if 'fn' in d:
        FILE_NAME = d['fn']
        del d['fn']

    FILE_NAME = f'graphs/{FILE_NAME}'

    # python main.py [bee] [fn] [it] [ps] [ep] [gp] [eb] [gb] [max_b] [max_c] [a_thr] [d_thr]
    if ALGO_TYPE == ALGO_BEE:
        G, number_of_vertices = get_graph_edges(FILE_NAME)
        solutions = bees_optimization_algorithm(G, number_of_vertices, **d)
        for solution in solutions:
            print(f'{solution.solution}   {solution.profitability}')

    # python main.py [gen] [fn] [epoch] [size] [children] [maxb] [maxc]
    elif ALGO_TYPE == ALGO_GEN:
        evolve(*get_graph(FILE_NAME), **d)
    else:
        print(f'Wrong argument! Use: python main.py [{ALGO_BEE}|{ALGO_GEN}]')
        exit(1)