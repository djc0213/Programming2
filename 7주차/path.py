import os

def get_dnames():
    allnames = os.listdir('.')
    print('allnames:', allnames)
    dnames = [name for name in allnames
          if os.path.isdir(name)]
###if os.path.isdir(name)은 directory name이면 가져와라는 뜻이다
    print('dnames:', dnames)
    return dnames

def get_fnames_from_dnames(dnames):
    fnames_all = []
    for dname in dnames:
        fnames = os.listdir(dname)
        fnames_all += [os.path.join(dname, fname) for fname in fnames]
        print(fnames_all)
        return fnames_all
    
dnames = get_dnames()
fnames = get_fnames_from_dnames(dnames)
print('\n'.join(fnames))