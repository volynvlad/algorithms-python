from packing_task import packing_task
import random


def test_nest_fit():
    n = 10

    weights = [random.uniform(0.01, 1) for _ in range(n)]

    next_fit_result = packing_task.next_fit(weights)

    assert [sum(x) <= 1 for x in next_fit_result] == [True] * len(next_fit_result)


def test_first_fit():
    n = 10

    weights = [random.uniform(0.01, 1) for _ in range(n)]

    first_fit_result = packing_task.first_fit(weights)

    assert [sum(x) <= 1 for x in first_fit_result] == [True] * len(first_fit_result)


def test_best_fit():
    n = 10

    weights = [random.uniform(0.01, 1) for _ in range(n)]

    best_fit_result = packing_task.best_fit(weights)

    assert [sum(x) <= 1 for x in best_fit_result] == [True] * len(best_fit_result)
