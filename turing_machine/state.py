from enum import Enum


class StateType(Enum):
    Start = 0
    Empty = 1
    Final_y = 2
    Final_n = 3


class State:
    def __init__(self, state_type, description):
        self.state_type = state_type
        self.description = description
