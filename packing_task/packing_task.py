import random
import numpy as np


def next_fit(weights, c=1):
    current_container = 0
    containers = [[]]
    for weight in weights:
        if sum(containers[current_container]) + weight > c:
            current_container += 1
            containers.append([])
        containers[current_container].append(weight)
    return containers


def first_fit(weights, c=1):
    containers = [[] for _ in range(len(weights))]

    i = 0
    j = 0
    while j < len(weights):
        while i < len(containers):
            if sum(containers[i]) + weights[j] <= c:
                containers[i].append(weights[j])
                j += 1
                i = -1
                if j == len(weights):
                    break
            i += 1

    return containers


# first fit (с упоряд)
def ordered_first_fit(weights, c=1):
    containers = [[] for _ in range(len(weights))]
    weights = np.array(weights)
    weights = -np.sort(-weights)

    i = 0
    j = 0
    while j < len(weights):
        while i < len(containers):
            if sum(containers[i]) + weights[j] <= c:
                containers[i].append(weights[j])
                j += 1
                i = -1
                if j == len(weights):
                    break
            i += 1

    return containers


def best_fit(weights, c=1):
    containers = [[] for _ in range(len(weights))]

    i = 0
    j = 0
    while j < len(weights):
        while i < len(containers):
            free_spaces = [c - weights[j] - sum(x) for x in containers]
            for i in range(len(free_spaces)):
                if free_spaces[i] < 0:
                    free_spaces[i] = c + 0.01
            containers[int(np.argmin(free_spaces))].append(weights[j])
            j += 1
            i = -1
            if j == len(weights):
                break
        i += 1

    return containers


if __name__ == '__main__':
    n = 10

    weights = [random.uniform(0.01, 1) for _ in range(n)]
    # n = 4
    # weights = [0.5, 0.7, 0.5, 0.3]

    next_fit_result = next_fit(weights)
    first_fit_result = first_fit(weights)
    ordered_first_fit_result = ordered_first_fit(weights)
    best_fit_result = best_fit(weights)

    first_fit_result = [x for x in first_fit_result if len(x) != 0]
    ordered_first_fit_result = [x for x in ordered_first_fit_result if len(x) != 0]
    best_fit_result = [x for x in best_fit_result if len(x) != 0]

    print(f"weights = {weights}")
    print('-' * 25)
    print("next fit")
    [print(x) for x in next_fit_result]
    print(f"number of containers needed - {len(next_fit_result)}")
    print("first fit")
    [print(x) for x in first_fit_result]
    print(f"number of containers needed - {len(first_fit_result)}")
    print("ordered first fit")
    [print(x) for x in ordered_first_fit_result]
    print(f"number of containers needed - {len(ordered_first_fit_result)}")
    print("best fit")
    [print(x) for x in best_fit_result]
    print(f"number of containers needed - {len(best_fit_result)}")

