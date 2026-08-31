num = int(input('enter number: '))

sum = 0

for i in range (num+1):
    temp = sum
    sum += i 
    print(f'{temp} + {i} = {sum}')
