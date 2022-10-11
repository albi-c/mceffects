import enum

from .position import Position


class TokenType(enum.Flag):
    ID = enum.auto()
    NUM = enum.auto()

    TILDE = enum.auto()
    CARET = enum.auto()
    DOLLAR = enum.auto()

    COLON = enum.auto()
    COMMA = enum.auto()

    LPAREN = enum.auto()
    RPAREN = enum.auto()
    LBRACE = enum.auto()
    RBRACE = enum.auto()
    LBRACK = enum.auto()
    RBRACK = enum.auto()

    OPERATOR = enum.auto()


class Token:
    type: TokenType
    val: str
    pos: Position

    SINGLE_CHAR = {
        "~": TokenType.TILDE,
        "^": TokenType.CARET,
        "$": TokenType.DOLLAR,

        ":": TokenType.COLON,
        ",": TokenType.COMMA,

        "(": TokenType.LPAREN,
        ")": TokenType.RPAREN,
        "{": TokenType.LBRACE,
        "}": TokenType.RBRACE,
        "[": TokenType.LBRACK,
        "]": TokenType.RBRACK,

        "+": TokenType.OPERATOR,
        "-": TokenType.OPERATOR,
        "*": TokenType.OPERATOR,
        "/": TokenType.OPERATOR
    }

    def __init__(self, type_: TokenType, val: str, pos: Position):
        self.type = type_
        self.val = val
        self.pos = pos

    def __repr__(self):
        return f"['{self.val}', {self.type}]"
