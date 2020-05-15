import random
import time

from local_minimum.tsp import tsp
from graph.matrix_graph import GraphAdjMatrix


if __name__ == "__main__":
    number_nodes = 500
    random_range = [1, 10]
    matrix = [[0 for x in range(number_nodes)] for y in range(number_nodes)]

    graph = GraphAdjMatrix(matrix, number_nodes)

    sum_l = 0
    iter_num = 40
    coef = 6

    start_end = 0
    for k in range(iter_num):
        for i in range(number_nodes):
            for j in range(i + 1, number_nodes):
                graph.add_double_edge((i, j), weight=random.randint(*random_range))
        start = time.time()
        local_minimum_tsp = tsp(graph, coef)
        end = time.time()
        start_end = start_end + end - start
        sum_l += graph.get_cycle_weight(local_minimum_tsp)

    print(start_end)
    with open('results', 'a+') as f:
        f.write(f"mean_weight = {sum_l / iter_num} number_nodes = {number_nodes} coef = {coef} mean_time = {(start_end) / iter_num}\n")
