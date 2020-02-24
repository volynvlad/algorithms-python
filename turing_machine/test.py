from algorithms_python.turing_machine.turing_machine import TuringMachine

matrix_ = [[("qy", "a", 0), ("q1", "a", 0), ("q1", "b", 0), ("q1", "c", 0)],
           [("qy", "a", 0), ("q2", "#", 1), ("q2", "#", 1), ("q2", "#", 1)],
           [("qy", "#", 0), ("q1", "#", 1), ("q1", "#", 1), ("q1", "#", 1)]]
dictionary_ = ["a", "b", "c"]
states_ = ["q0", "q1", "q2"]

turing_machine = TuringMachine(dictionary_, states_, matrix_)


def test_even_case():
    assert turing_machine.start("abcabc").count("a") == 1


def test_odd_case():
    assert turing_machine.start("abc").count("a") == 0


def test_empty_case():
    assert turing_machine.start("").count("a") == 1

