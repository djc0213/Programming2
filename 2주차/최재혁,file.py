file_jh = open('name_student.txt', 'w')
file_jh.write('jh')
file_jh.close()
file_km = open('data/name_TA.txt', 'w')
file_km.write('km')
file_km.close()
path = 'C:/Users/socce/OneDrive/문서/School/연세대학교/2023-1 3학년 2학기/정보프로그래밍심화/name_yonsei.txt'
file_abs = open(path, 'w')
file_abs.write('yonsei')
file_abs.close()

input_file = open('myfile.txt', 'r')
lines = input_file.readlines()
input_file.close()
print(lines)
for line in lines:
    print(line)

with open('myfile.txt', 'r') as f:
    lines = f.readlines()
    print(lines)