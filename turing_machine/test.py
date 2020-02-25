from algorithms_python.turing_machine.turing_machine import TuringMachine

ft_matrix = [[("qy", "a", 0), ("q1", "a", 0), ("q1", "b", 0), ("q1", "c", 0)],
             [("qy", "a", 0), ("q2", "#", 1), ("q2", "#", 1), ("q2", "#", 1)],
             [("qy", "#", 0), ("q1", "#", 1), ("q1", "#", 1), ("q1", "#", 1)]]
ft_dictionary = ["a", "b", "c"]
ft_states = ["q0", "q1", "q2"]

first_task = TuringMachine(ft_dictionary, ft_states, ft_matrix)


def test_even_case():
    """
    test for even case for the first task
    """
    assert first_task.start("abcabc").count("a") == 1


def test_odd_case():
    """
    test for odd case for the first task
    """
    assert first_task.start("abc").count("a") == 0


def test_empty_case():
    """
    test for empty case for the first task
    """
    assert first_task.start("").count("a") == 1
