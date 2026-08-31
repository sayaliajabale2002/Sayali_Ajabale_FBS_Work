num = int(input('enter a number: '))
temp = num 
rev = 0

while(temp > 0):
    d = temp % 10
    rev = rev*10 + d 
    temp //= 10

if(num == rev):
    print(f'{num} is palindrome number')
else:
    print(f'{num} is not palindrome number')