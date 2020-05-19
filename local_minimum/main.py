import random
import time

from local_minimum.tsp import tsp
from graph.matrix_graph import GraphAdjMatrix


if __name__ == "__main__":
    number_nodes = 100
    random_range = [0, number_nodes]
    random.seed = 42
    matrix = [[0 for x in range(number_nodes)] for y in range(number_nodes)]

    graph = GraphAdjMatrix(matrix, number_nodes)

    ratio = 0
    iter_num = 16

    start_end = 0
    graph_weight = 0
    for k in range(iter_num):
        for i in range(number_nodes):
            graph.add_double_edge((i, i), weight=0)
            for j in range(i + 1, number_nodes):
                graph.add_double_edge((i, j), weight=random.randint(*random_range))

        start = time.time()
        local_minimum_tsp = tsp(graph)
        end = time.time()
        start_end = start_end + end - start
        ratio = ratio + graph.get_cycle_weight(local_minimum_tsp) / graph.get_graph_weight()

    print(start_end)
    with open('results', 'a+') as f:
        f.write(f"mean_ration = {ratio / iter_num} number_nodes = {number_nodes} mean_time = {start_end / iter_num}\n")
