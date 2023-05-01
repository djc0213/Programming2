import os
from os.path import join as ospj

dname_cwd = os.getcwd()
dname = 'emails'
fnames_email = os.listdir(dname)
print(fnames_email)
for fname in fnames_email:
    print(dname_cwd)
    print(dname)
    print(fname)
    fname_joined = ospj(dname_cwd, dname, fname)
    print(fname_joined)
    fname_wo_ext, ext = os.path.splitext(fname_joined)
    fname_py = fname_wo_ext + '.py'
    print(fname_py)