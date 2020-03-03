"""
turing_machine module
"""
import pandas as pd


class TuringMachine:
    """
    TuringMachine
    """
    def __init__(self, dictionary, states, matrix, head_tape, tail_tape):
        self.dictionary = ["#"] + dictionary
        self.states = states
        self.matrix = matrix
        self.table = pd.DataFrame(self.matrix, columns=self.dictionary,
                                  index=self.states)
        print(self.table)
        self.tape = []
        self.head_tape = head_tape or []
        self.tail_tape = tail_tape or ["#"] * 5

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
        self.display(self.tape)
        print(state, self.tape[position])
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
        self.tape = self.head_tape + [c for c in word if c in self.dictionary] + self.tail_tape

        self.run(current_state, head_position)
        return ''.join(self.tape)
