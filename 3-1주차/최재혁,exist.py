import os

fname = 'emails/jaehyeok.txt'
if os.path.exists(fname):
    choice = input(f'{fname} already exist. overwrite? (y/n)')
    if choice == 'n':
        print('abort')
        exit()
    else:
        print('overwriting...')
print(os.path.exists('emails'))
print(os.path.exists('emails/jh.txt'))
print(os.path.exists('emails/jaehyeok.txt'))

with open(fname, 'w') as f:
    f.write('some dummy overwritten text')