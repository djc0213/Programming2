import os

os.chdir('..')

dname_current = os.getcwd()
print('current path: ', dname_current)

ldir = os.listdir()
print(ldir)