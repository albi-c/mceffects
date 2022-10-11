class Position:
    line: int
    column: int
    length: int
    code: str

    def __init__(self, line: int, column: int, length: int, code: str):
        self.line = line
        self.column = column
        self.length = length
        self.code = code

    def arrows(self) -> str:
        return f"{' ' * self.column}{'^' * self.length}"

    def code_section(self) -> str:
        return self.code[self.column:self.column+self.length]
