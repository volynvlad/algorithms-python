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

FIRST_TASK = TuringMachine(FT_DICTIONARY, FT_STATES, FT_MATRIX, None, None)


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


ST_MATRIX = [[("q0", "#", 1), ("q0", "a", 1), ("q0", "b", 1), ("q0", "c", 1), ("qa", "^", -1), (), ()],  # q0
             [("qb0", "#", 1), ("q*a", "*", 1), ("qa", "b", -1), ("qa", "c", -1), (), (), ("qa", "*", -1)],  # qa
             [(), ("q*a", "a", 1), ("q*a", "b", 1), ("q*a", "c", 1), ("q*a", "^", 1), ("q^a", "a", -1), ("q*a", "*", 1)],  # q*a
             [(), ("q^a", "a", -1), (), (), ("qa", "^", -1), (), ()],  # q^a
             [(), ("qb0", "a", 1), ("qb0", "b", 1), ("qb0", "c", 1), ("qb", "^", -1), (), ("qb0", "*", 1)],  # qb0
             [("qc0", "#", 1), (), ("q*b", "*", 1), ("qb", "c", -1), (), (), ("qb", "*", -1)],  # qb
             [(), ("q*b", "a", 1), ("q*b", "b", 1), ("q*b", "c", 1), ("q*b", "^", 1), ("q^b", "b", -1), ("q*b", "*", 1)],  # q*b
             [(), ("q^b", "a", -1), ("q^b", "b", -1), (), ("qb", "^", -1), (), ()],  # q^b
             [(), ("qc0", "a", 1), ("qc0", "b", 1), ("qc0", "c", 1), ("qc", "^", -1), (), ("qc0", "*", 1)],  # qc0
             [("qy", "#", 0), (), (), ("q*c", "*", 1), (), (), ("qc", "*", -1)],  # qc
             [(), ("q*c", "a", 1), ("q*c", "b", 1), ("q*c", "c", 1), ("q*c", "^", 1), ("q^c", "c", -1), ("q*c", "*", 1)],  # q*c
             [(), ("q^c", "a", -1), ("q^c", "b", -1), ("q^c", "c", -1), ("qc", "^", -1), (), ()],  # q^c
             ]
ST_DICTIONARY = ["a", "b", "c", "^", "_", "*"]
ST_STATES = ["q0", "qa", "q*a", "q^a", "qb0", "qb", "q*b", "q^b", "qc0", "qc", "q*c", "q^c"]

ST_HEAD_TAPE = ["#"]
ST_TAIL_TAPE = ["^"] + ["_"] * 64
SECOND_TASK = TuringMachine(ST_DICTIONARY, ST_STATES, ST_MATRIX, ST_HEAD_TAPE, ST_TAIL_TAPE)


def test_a():
    """
    test for the second task
    """
    result = SECOND_TASK.start("aca")

    assert result.replace("*", "").replace("_", "").replace("#", "").replace("^", "") == "aac"


def test_b():
    """
    test for the second task
    """
    result = SECOND_TASK.start("bcaca")

    assert result.replace("*", "").replace("_", "").replace("#", "").replace("^", "") == "aabcc"


def test_c():
    """
    test for the second task
    """
    result = SECOND_TASK.start("cacabb")

    assert result.replace("*", "").replace("_", "").replace("#", "").replace("^", "") == "aabbcc"


def test_empty():
    """
    test for the second task
    """

    result = SECOND_TASK.start("")

    assert result.replace("*", "").replace("_", "").replace("#", "").replace("^", "") == ""
