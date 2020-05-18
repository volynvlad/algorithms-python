from graph.matrix_graph import GraphAdjMatrix


def tsp(input_graph: GraphAdjMatrix):
    if input_graph.size <= 3:
        return list(range(input_graph.size))
    curr_solution = list(range(input_graph.size))
    curr_solution_weight = input_graph.get_cycle_weight(curr_solution)

    best_neighbor = curr_solution
    best_neighbor_weight = curr_solution_weight

    while True:
        j = 0
        for i in range(j + 2, input_graph.size + j - 1):
            # neighbor_sol = curr_solution.copy()
            # neighbor_sol[j], neighbor_sol[i % input_graph.size] = neighbor_sol[i % input_graph.size], neighbor_sol[j]

            # swap to get neighbor
            curr_solution[j], curr_solution[i % input_graph.size] = curr_solution[i % input_graph.size], curr_solution[j]

            neighbor_sol_weight = input_graph.get_cycle_weight(curr_solution)
            best_neighbor_weight = input_graph.get_cycle_weight(best_neighbor)
            if neighbor_sol_weight < best_neighbor_weight:
                best_neighbor = curr_solution.copy()
                best_neighbor_weight = neighbor_sol_weight

            # swap again to get initial solution
            curr_solution[j], curr_solution[i % input_graph.size] = curr_solution[i % input_graph.size], curr_solution[j]

        # update current solution
        if best_neighbor_weight < curr_solution_weight:
            curr_solution = best_neighbor.copy()
            curr_solution_weight = best_neighbor_weight
        else:
            break
        j += 1

    return curr_solution
