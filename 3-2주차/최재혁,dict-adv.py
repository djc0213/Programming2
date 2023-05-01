from munch import Munch
from pprint import pprint

def print_info (name, phone, email):
    print('name:', name)
    print('phone:', phone)
    print('email:', email)

jh = {'name': 'jaehyeok,',
      'phone': '01093245811',
      'email': 'jdc13@yonsei.ac.kr'}

print(jh)
pprint(jh)
print('email:', jh['email'])

jh = Munch()
jh.name = 'jaehyeok'
jh.phone = '01093245811'
jh.email = 'jdc13@yonsei.ac.kr'
print(jh)
print('email:', jh.email)
print('email:', jh['email'])
print_info(**jh)
pprint(jh)