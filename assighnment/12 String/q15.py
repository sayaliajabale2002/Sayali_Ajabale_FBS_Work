s1 = input('enter string 1: ')
s2 = input('enter string 2: ')

count1 = 0
count2 = 0
for i in s1:
    count1 += 1
for j in s2:
    count2 += 1

if(count1 > count2):
    print(f'lagest string is {s1}')
elif(count2 > count1):
    print(f'largest string is {s2}')
else:
    print('Both string have same length')