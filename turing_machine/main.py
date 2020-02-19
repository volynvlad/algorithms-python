import pandas as pd


def print_tape(tape):
    print(''.join(tape))


def turing_machine(dataframe, state, position, tape):
    if state == "qy":
        return
    next_state, letter, move_position = dataframe[tape[position]][state]
    tape[position] = letter
    position += move_position
    print_tape(tape)
    turing_machine(dataframe, next_state, position, tape)


word = "abcabc"
dictionary = ["a", "b", "c"]
table = [[("qy", "a", 0), ("q1", "a", 0), ("q1", "b", 0), ("q1", "c", 0)],
         [("qy", "a", 0), ("q2", "#", 1), ("q2", "#", 1), ("q2", "#", 1)],
         [("qy", "#", 0), ("q1", "#", 1), ("q1", "#", 1), ("q1", "#", 1)]]
states = ["q0", "q1", "q2"]


def first_task(table, word, dictionary, states):
    head_position = 0
    current_state = "q0"
    tape = [c for c in word if c in dictionary] + ["#"] * 5
    table = pd.DataFrame(table, columns=["#"] + dictionary, index=states)

    print(table)

    print_tape(tape)

    turing_machine(table, current_state, head_position, tape)


first_task(table, word, dictionary, states)
word = "abc"
print("------------")
first_task(table, word, dictionary, states)
