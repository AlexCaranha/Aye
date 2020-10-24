import sys
from inspect import getmembers, isfunction

def print_name(name):
    print(name)

def print_age(age):
    print(age)

current_module = sys.modules[__name__]
functions_list = [o for o in getmembers(current_module) if isfunction(o[1])]

print(functions_list)