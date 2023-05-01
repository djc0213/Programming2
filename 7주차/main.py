from utils import functions as ufunc
from info import functions as ifunc

def say_hi():
    print('Hi from main')

ufunc.print_whose('watch', 'his')
ufunc.say_hi()
ifunc.say_hi()
say_hi()

print(ufunc.__name__)
print(ifunc.__name__)
print(__name__)