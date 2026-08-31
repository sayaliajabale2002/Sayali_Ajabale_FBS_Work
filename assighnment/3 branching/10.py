male_age = int(input('enter male age: '))
female_age = int(input('enter female age: '))

if(male_age >= 21):
    if(female_age >=18):
        print('person is eligible to marry')
    else:
        print('female age should be greater or equal to 18')
else:
    print('male age should be greater or equal to 21')