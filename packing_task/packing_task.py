import random
import numpy as np


def next_fit(weights):
    current_container = 0
    containers = [[]]
    for weight in weights:
        if sum(containers[current_container]) + weight > 1:
            current_container += 1
            containers.append([])
        containers[current_container].append(weight)
    return containers


def fest_fit(weights):
    containers = [[] for _ in range(len(weights))]

    i = 0
    j = 0
    while j < len(weights):
        while i < len(containers):
            if sum(containers[i]) + weights[j] <= 1:
                containers[i].append(weights[j])
                j += 1
                i = -1
                if j == len(weights):
                    break
            i += 1
        j += 1

    return containers


def best_fit(weights):
    containers = [[] for _ in range(len(weights))]
    weights = np.array(weights)
    weights = -np.sort(-weights)

    i = 0
    j = 0
    while j < len(weights):
        while i < len(containers):
            if sum(containers[i]) + weights[j] <= 1:
                containers[i].append(weights[j])
                j += 1
                i = -1
                if j == len(weights):
                    break
            i += 1
        j += 1

    return containers


if __name__ == '__main__':
    n = 10

    weights = [random.uniform(0.01, 1) for _ in range(n)]

    next_fit_result = next_fit(weights)
    fest_fit_result = fest_fit(weights)
    best_fit_result = best_fit(weights)

    print(f"weights = {weights}")
    print("next fit")
    [print(x) for x in next_fit_result]
    print("fest fit")
    [print(x) for x in fest_fit_result]
    print("best fit")
    [print(x) for x in best_fit_result]
