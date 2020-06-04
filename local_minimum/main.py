import random
import time

from local_minimum.tsp import tsp
from graph.matrix_graph import GraphAdjMatrix


if __name__ == "__main__":
    # number_nodes = 100
    # random_range = [0, number_nodes]
    # random.seed = 42
    # matrix = [[0 for x in range(number_nodes)] for y in range(number_nodes)]
    #
    # graph = GraphAdjMatrix(matrix, number_nodes)
    #
    # graph_weight = 0
    # for i in range(number_nodes):
    #     graph.add_double_edge((i, i), weight=0)
    #     for j in range(i + 1, number_nodes):
    #         graph.add_double_edge((i, j), weight=random.randint(*random_range))
    #
    #     local_minimum_tsp = tsp(graph)
    #     print(graph.get_cycle_weight(local_minimum_tsp))
    #     print(graph.get_graph_weight())

    number_nodes = 10
    matrix = [[0 for x in range(number_nodes)] for y in range(number_nodes)]

    graph = GraphAdjMatrix(matrix, number_nodes)

    for i in range(number_nodes):
        for j in range(i + 1, number_nodes):
            graph.add_double_edge((i, j), weight=10)

    local_min_tsp = tsp(graph)

    print(f"solution = {local_min_tsp}")
    print(f"weight = {graph.get_cycle_weight(local_min_tsp)}")
    print('-' * 30)

    cycle = [2, 4, 6, 8, 0, 1, 3, 5, 7, 9]
    for i in range(len(cycle)):
        graph.add_double_edge((cycle[i - 1], cycle[i]), weight=1)

    local_min_tsp = tsp(graph)

    print(f"solution = {local_min_tsp}")
    print(f"weight = {graph.get_cycle_weight(local_min_tsp)}")
    print('-' * 30)

    cycle = [2, 3, 7, 1, 0, 5, 6, 8, 4, 9]
    for i in range(len(cycle)):
        graph.add_double_edge((cycle[i - 1], cycle[i]), weight=1)

    local_min_tsp = tsp(graph)

    print(f"solution = {local_min_tsp}")
    print(f"weight = {graph.get_cycle_weight(local_min_tsp)}")
