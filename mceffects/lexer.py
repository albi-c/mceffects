import string

from .token import Token, TokenType, Position
from .error import Error


class Lexer:
    code: str
    i: int
    line: int
    char: int

    ID_CHARS = string.ascii_lowercase
    ID_CHARS_START = ID_CHARS + "."

    NUM_CHARS = string.digits + "."
    NUM_CHARS_START = NUM_CHARS + "-"

    def next_char(self, char: str | None = None) -> str:
        self.i += 1

        if self.i >= len(self.code):
            return ""

        ch = self.code[self.i]
        if char is not None and ch not in char:
            Error.unexpected_character(self.make_position(1), ch)

        self.char += 1
        if ch == "\n":
            self.char = 0
            self.line += 1

        return ch

    def lookahead_char(self, char: str | None = None) -> str | bool:
        if self.i + 1 >= len(self.code):
            return ""

        if char is not None:
            if self.code[self.i + 1] in char:
                self.next_char()
                return True

            return False

        return self.code[self.i + 1]

    def prev_char(self):
        if self.i > -1:
            self.i -= 1
            self.char -= 1

    def make_position(self, n: int) -> Position:
        return Position(self.line, self.char, n, self.code.splitlines()[self.line])

    def make_token(self, type_: TokenType, value: str) -> Token:
        return Token(type_, value, self.make_position(len(value)))

    def lex(self, code: str) -> list[Token]:
        self.code = code
        self.i = -1
        self.line = 0
        self.char = 0

        tokens = []
        while ch := self.lookahead_char():
            if ch == "":
                break

            if not ch.strip():
                self.next_char()
                continue

            if ch == "#":
                self.lex_until_eol()
                continue

            if ch in self.ID_CHARS_START and (token := self.lex_id()) is not None:
                tokens.append(self.make_token(TokenType.ID, token))

            elif ch in self.NUM_CHARS_START and (token := self.lex_num()) is not None:
                tokens.append(self.make_token(TokenType.NUM, token))

            elif ch in Token.SINGLE_CHAR:
                self.next_char()
                tokens.append(self.make_token(Token.SINGLE_CHAR[ch], ch))

            else:
                Error.unexpected_character(self.make_position(1), ch)

        return tokens

    def lex_until_eol(self):
        while self.next_char() != "\n":
            pass

    def lex_id(self):
        token = self.next_char()

        if not self.lookahead_char() in self.ID_CHARS and token == ".":
            return None

        while (ch := self.lookahead_char()) in self.ID_CHARS:
            self.next_char()
            token += ch

        return token

    def lex_num(self):
        token = self.next_char()

        if not self.lookahead_char() in self.NUM_CHARS and token == "-":
            return None

        while (ch := self.lookahead_char()) in self.NUM_CHARS:
            self.next_char()

            if "." in token and ch == ".":
                Error.unexpected_character(self.make_position(1), ch)

            token += ch

        return token
