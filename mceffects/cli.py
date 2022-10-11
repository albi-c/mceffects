from .lexer import Lexer


def main():
    print(Lexer().lex(".interp (x, -5 : 5 : 0.1) { dust [1, 0, 1, 0.7] (~ - x) }"))
