"""
This is a module to be used as a reference for building other modules
"""


def foo():
    """docstring for foo"""
    return 'foo'


class Bar():
    """docstring for Bar"""
    def __init__(self, arg):
        super().__init__()
        self.arg = arg
