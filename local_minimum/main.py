import random

from local_minimum.tsp import tsp
from graph.matrix_graph import GraphAdjMatrix


if __name__ == "__main__":
    number_nodes = 6
    random_range = [1, 10]
    matrix = [[0 for x in range(number_nodes)] for y in range(number_nodes)]

    graph = GraphAdjMatrix(matrix, number_nodes)

    for i in range(number_nodes):
        for j in range(i + 1, number_nodes):
            graph.add_double_edge((i, j), weight=random.randint(*random_range))

    local_minimum_tsp = tsp(graph)


