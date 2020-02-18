import pandas as pd
from algorithms_python.turing_machine.state import StateType


class TuringMachine:
    def __init__(self, states, tape):
        self.states = states
        self.tape = tape

    def get_tape(self):
        return self.tape.get_tape()

