from graph.matrix_graph import GraphAdjMatrix


def tsp(input_graph: GraphAdjMatrix, coef):
    if input_graph.size <= 3:
        return list(range(input_graph.size))
    curr_solution = list(range(input_graph.size))
    curr_solution_weight = input_graph.get_cycle_weight(curr_solution)

    best_neighbor = curr_solution
    best_neighbor_weight = curr_solution_weight
    while True:
        # print(f"curr_solution = {curr_solution}, weight = {curr_solution_weight}")
        for i in range(0, input_graph.size, coef):
            neighbor_sol = curr_solution.copy()
            neighbor_sol[i], neighbor_sol[i + 1] = neighbor_sol[i + 1], neighbor_sol[i]

            neighbor_sol_weight = input_graph.get_cycle_weight(neighbor_sol)
            best_neighbor_weight = input_graph.get_cycle_weight(best_neighbor)
            if neighbor_sol_weight < best_neighbor_weight:
                best_neighbor = neighbor_sol
                best_neighbor_weight = neighbor_sol_weight

        if best_neighbor_weight < curr_solution_weight:
            curr_solution = best_neighbor
            curr_solution_weight = best_neighbor_weight
        else:
            break

    return curr_solution
