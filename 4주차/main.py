#import utils.functions
#import info.functions
from utils import functions as ufunc
from info import functions as ifunc

def say_hi():
    print('Hi from main')

#utils.function.print_whose('watch', 'his')
ufunc.print_whose('watch', 'his')
#print(f'side = {utils.funcitons.side}')
#utils.functions.say_hi()
#info.functions.say_hi()
ufunc.say_hi()
ifunc.say_hi()
say_hi()

print(ufunc.__name__)
print(ifunc.__name__)
print(__name__)