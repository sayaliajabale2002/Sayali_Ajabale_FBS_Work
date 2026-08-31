# let userid = sayali@07
# password = sayali123
import random

user_id = input("enter valid user id: ")
password = input('enter valid password: ')

if(user_id=='sayali@07' and password=='sayali123'):
    print('valid user id & password')
    random_number = random.randint(1000,9999)
    print(f'generated number = {random_number}')
    num = int(input('enter above generated number: '))
    if(num == random_number):
        print('success')
    else:
        print('failed')
else:
    print('invalid user id & password')
