from functools import partial

def square(x):
    return x**2

def print_mine(some_string):
    print('my', some_string)

def say_hi():
    print('Hi')

def print_whose(item, owner='mine'):
    print(f'{item} is {owner}.')