num = int(input('enter number: '))

num1 = 0
num2 = 1

print(f'{num1}, {num2}, ', end='')

for i in range (2,num):
    term = num1 + num2 
    num1 = num2 
    num2 = term
    print(f'{term}, ', end='')