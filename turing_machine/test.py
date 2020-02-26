"""
test for this tasks
1.5. Г={a,b,c}. Если P – слово чётной длины (0, 2, 4, ...), то выдать ответ a,
иначе – пустое слово.
2.6. Г={a,b,c}. Преобразовать слово P так, чтобы сначала шли все символы a,
затем – все символы b и в конце – все символы c.
"""


from algorithms_python.turing_machine.turing_machine import TuringMachine

FT_MATRIX = [[("qy", "a", 0), ("q1", "a", 0), ("q1", "b", 0), ("q1", "c", 0)],
             [("qy", "a", 0), ("q2", "#", 1), ("q2", "#", 1), ("q2", "#", 1)],
             [("qy", "#", 0), ("q1", "#", 1), ("q1", "#", 1), ("q1", "#", 1)]]
FT_DICTIONARY = ["a", "b", "c"]
FT_STATES = ["q0", "q1", "q2"]

FIRST_TASK = TuringMachine(FT_DICTIONARY, FT_STATES, FT_MATRIX)


def test_even_case():
    """
    test for even case for the first task
    """
    assert FIRST_TASK.start("abcabc").count("a") == 1


def test_odd_case():
    """
    test for odd case for the first task
    """
    assert FIRST_TASK.start("abc").count("a") == 0


def test_empty_case():
    """
    test for empty case for the first task
    """
    assert FIRST_TASK.start("").count("a") == 1


ST_MATRIX = [[("q0", "#", 1), ("q1", "a", 0), ("q1", "b", 0), ("q1", "c", 0)],  # q0
             [("q7", "#", -1), ("q1", "a", 1), ("q2", "b", 1), ("q4", "c", 1)],  # q1
             [("q7", "#", -1), ("q3", "b", -1), ("q1", "b", 0), ("q1", "c", 0)],  # q2
             [("q7", "#", -1), (), ("q1", "a", 0), ()],  # q3
             [("q7", "#", -1), ("q5", "c", -1), ("q6", "c", -1), ("q1", "c", 0)],  # q4
             [("q7", "#", -1), (), (), ("q1", "a", 0)],  # q5
             [("q7", "#", -1), (), (), ("q1", "b", 0)],  # q6
             [("q0", "#", 1), ("q7", "a", -1), ("q7", "b", -1), ("q7", "c", -1)]]  # q7
ST_DICTIONARY = ["a", "b", "c"]
ST_STATES = ["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7"]

SECOND_TASK = TuringMachine(ST_DICTIONARY, ST_STATES, ST_MATRIX)


def test_default_case():
    """
    test for the second task
    """
    result = SECOND_TASK.start("#bcaca")
    for i in range(len(result) - 1):
        if result[i] != "#":
            assert result[i] <= result[i + 1]

