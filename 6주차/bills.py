from pprint import pprint

def breakdown(amount: float):
    amount *= 100
    bills = {}
    units = [100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]
    units = [unit * 100 for unit in units]
    for unit in units:
        count = amount // unit
        amount -= count * unit
        bills[unit/100] = count
    return bills

number2word = {1: 'one',
               2: 'two',
               3: 'three',
               4: 'four',
               5: 'five',
               6: 'six',
               7: 'seven',
               8: 'eight',
               9: 'nine',}

def read_number(number):
    if number == 1:
        return 'one'
    elif number == 2:
        return 'two'
    else:
        return 'haha'

def trim_unit(unit):
    if int(unit) == unit:
        return int(unit)
    else:
        return unit

def read_bills(bills):
    for unit, count in bills.items():
        if count == 0:
            continue
        word = number2word[int(count)]
        unit = trim_unit(unit)
        unit_name = 'bills' if isinstance(unit, int) else 'coins'
        print(f'{word} ${unit} {unit_name}')

amount = float(input('input $:'))
bills = breakdown(amount)
pprint(bills)
read_bills(bills)