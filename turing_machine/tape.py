from algorithms_python.turing_machine.direction import Direction


class Tape:
    def __init__(self, word, alphabet):
        self.alphabet = set(alphabet + "#")
        self.__init_tape(word)
        self.head_position = 0

    def __init_tape(self, word):
        self._tape = []
        self._tape.extend([c for c in word if c in self.alphabet])
        self._tape.extend(["#"] * 5)

    def get_tape(self):
        return ''.join(self._tape)

    def write(self, letter):
        if self.head_position < 1 or letter not in self.alphabet:
            return
        self._tape[self.head_position] = letter

        if self.head_position == len(self._tape) - 1:
            self._tape.append("#")

    def read(self):
        if self.head_position < 0 or self.head_position > len(self._tape) - 1:
            raise Exception()
        return self._tape[self.head_position]

    def move_head(self, direction):
        if direction == Direction.Right:
            self.head_position += 1
        elif direction == Direction.Left:
            self.head_position -= 1

        if self.head_position < 0:
            self.head_position = 0
        elif self.head_position > self.get_length() - 1:
            return

    def get_length(self):
        return len(self._tape)
