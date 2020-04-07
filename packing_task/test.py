from packing_task import packing_task
import random


def test_nest_fit():
    n = 10

    weights = [random.uniform(0.01, 1) for _ in range(n)]

    next_fit_result = packing_task.next_fit(weights)

    """
    print(weights)
    [print(x) for x in next_fit_result]
    print([sum(x) for x in next_fit_result])
    """

    assert [sum(x) <= 1 for x in next_fit_result] == [True] * len(next_fit_result)


def test_fest_fit():
    n = 10

    weights = [random.uniform(0.01, 1) for _ in range(n)]

    fest_fit_result = packing_task.fest_fit(weights)

    """
    print(weights)
    [print(x) for x in next_fit_result]
    print([sum(x) for x in next_fit_result])
    """

    assert [sum(x) <= 1 for x in fest_fit_result] == [True] * len(fest_fit_result)


def test_best_fit():
    n = 10

    weights = [random.uniform(0.01, 1) for _ in range(n)]

    best_fit_result = packing_task.best_fit(weights)

    """
    print(weights)
    [print(x) for x in next_fit_result]
    print([sum(x) for x in next_fit_result])
    """

    assert [sum(x) <= 1 for x in best_fit_result] == [True] * len(best_fit_result)
