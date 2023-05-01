from functools import partial

def square(x):
    return x**2

def print_mine(some_string):
    print('my', some_string)

def say_hi():
    print('Hi')

def print_whose(item, owner='mine'):
    print(f'{item} is {owner}.')

item_and_owner = {'item': 'iphone',
                  'owner': 'mine'}
print_whose(**item_and_owner)

print_his = partial(print_whose, owner='his')
print_hers = partial(print_whose, owner='hers')
print_yours = partial(print_whose, owner='yours')

def test_args(a, b, c, d, e):
    print(a, b, c, d, e)

test_args(1, 2, 3, 4, 5)
test_args(1, 2, 3, e=4, d=5)

test_partial = partial(test_args, 6, 7, e=10)
test_partial(8, 9)

odd_numbers = [1, 3, 5, 7, 9]
test_args(*odd_numbers)

print_mine('laptop')
print(print_mine('mouse'))

say_hi()

print_whose('laptop', 'his')
print_whose('laptop')
print('====paritial====')
print_his('laptop')
print_hers('laptop')
print_yours('laptop')

side = 5
area = square(side)
print(f'area of a square with a side {side} = {area}')