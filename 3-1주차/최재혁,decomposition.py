import os

def print_decomposition(path):
    print('filename: ', path)
    print('dirname: ', os.path.dirname(path))
    print('basename: ', os.path.basename(path))
fname_email = 'emails/jaehyeok.txt'
print_decomposition(fname_email)

dname_current = os.getcwd()
print_decomposition(dname_current)