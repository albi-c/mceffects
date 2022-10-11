from .position import Position


class Error(Exception):
    msg: str
    pos: Position | None

    def __init__(self, msg: str, pos: Position = None):
        self.msg = msg
        self.pos = pos

    def print(self):
        if self.pos is not None:
            print(f"Error on line {self.pos.line}, column {self.pos.column + 1}: {self.msg}")
            print(f"Here:\n{self.pos.code}\n{self.pos.arrows()}")
        else:
            print(f"Error: {self.msg}")

    @staticmethod
    def unexpected_character(pos: Position, ch: str):
        raise Error(f"Unexpected character [{ch}]", pos)
