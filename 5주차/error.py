try:
    odd_numbers = [1, 3, 5, 7, 9]
    print(odd_numbers[3] + 'abc')
    print(odd_numbers[6])
except TypeError as e:
    print('Type error happened.')
    print(e)
except Exception as e:
    print('Something wrong happened.')
    print(e)
print('Program continues.')