import glob

print(glob.glob('*.txt'))
print('='*10)
print(glob.glob('*.py'))
print('='*10)
fnames = glob.glob('emails/*.txt')
print(fnames)

for fname in fnames:
    with open(fname, 'r') as f:
        email = f.read()
        username, domain = email.split('@')
        print(f'{username}@korea.ac.kr')