import random

from graph.list_graph import GraphAdjList
from graph.matrix_graph import GraphAdjMatrix


def tsp(input_graph: GraphAdjMatrix):
    if input_graph.size <= 3:
        return list(range(input_graph.size))
    curr_solution = list(range(input_graph.size))  # 0 .. n-1

    best_neighbor = curr_solution
    while True:
        print(f"curr_solution = {curr_solution}, weight = {input_graph.get_cycle_weight(curr_solution)}")
        for i in range(0, input_graph.size // 2, 2):
            neighbor_sol = curr_solution.copy()
            neighbor_sol[i], neighbor_sol[i + 1] = neighbor_sol[i + 1], neighbor_sol[i]
            if input_graph.get_cycle_weight(neighbor_sol) < input_graph.get_cycle_weight(best_neighbor):
                best_neighbor = neighbor_sol

        if input_graph.get_cycle_weight(best_neighbor) < input_graph.get_cycle_weight(curr_solution):
            curr_solution = best_neighbor
        else:
            break

    return curr_solution
