class Operation:
    def __init__(self, current_state, current_letter,
                 new_state, new_letter, direction):
        self.current_state = current_state
        self.current_letter = current_letter
        self.new_state = new_state
        self.new_letter = new_letter
        self.direction = direction
