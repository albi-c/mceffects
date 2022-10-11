import pyperclip


class Output:
    _BUFFER: str = ""

    @staticmethod
    def _MODIFIER(s: str):
        return s

    @staticmethod
    def write(msg: str):
        Output._BUFFER += Output._MODIFIER(msg) + "\n"

    @staticmethod
    def write_modifier(func=None):
        Output._MODIFIER = func if func is not None else lambda x: x

    @staticmethod
    def clipboard():
        pyperclip.copy(Output._BUFFER)
        Output._BUFFER = ""

    @staticmethod
    def print():
        print(Output._BUFFER)
        Output._BUFFER = ""
