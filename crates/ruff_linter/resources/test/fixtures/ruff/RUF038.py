from typing import Literal


def func1(arg1: Literal[True, False]): 
    ...


def func2(arg1: Literal[True, False, True]): 
    ...


def func3() -> Literal[True, False]: 
    ...


def func4(arg1: Literal[True, False] | bool): 
    ...


def func5(arg1: Literal[False, True]):
    ...


def func6(arg1: Literal[True, False, "hello", "world"]):
    ...

# ok
def good_func1(arg1: bool): 
    ...


def good_func2(arg1: Literal[True]):
    ...
