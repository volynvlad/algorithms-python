"""
turing_machine module
"""
import pandas as pd


class TuringMachine:
    """
    TuringMachine
    """
    def __init__(self, dictionary, states, matrix):
        self.dictionary = dictionary
        self.states = states
        self.matrix = matrix
        self.table = pd.DataFrame(matrix, columns=["#"] + dictionary,
                                  index=states)
        self.tape = []

    @staticmethod
    def display(tape):
        """
        display tape as a string in the console
        """
        print(''.join(tape))

    def run(self, state, position):
        """
        run method
        """
        if state in ('qy', 'qn'):
            return
        next_state, letter, move_position = \
            self.table[self.tape[position]][state]
        self.tape[position] = letter
        position += move_position
        self.run(next_state, position)

    def start(self, word):
        """
        start method
        """
        head_position = 0
        current_state = "q0"
        self.tape = [c for c in word if c in self.dictionary] + ["#"] * 5

        self.run(current_state, head_position)
        return ''.join(self.tape)
