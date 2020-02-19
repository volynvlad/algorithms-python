import pandas as pd
from algorithms_python.turing_machine.state import StateType


class TuringMachine:
    def __init__(self, states, tape, dictionary, state_table):
        self.states = states
        self.tape = tape
        self.dictionary = dictionary
        self.state_table = state_table

    def get_tape(self):
        return self.tape.get_tape()

