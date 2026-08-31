num = int(input('enter number: '))

count = 0
temp = num 
while(temp > 0):
    temp //= 10 
    count += 1

# print(count)
temp = num 
sum = 0 

while(temp > 0):
    d = temp % 10 
    sum += d**count 
    temp //= 10 

if(num == sum):
    print(f'{num} is Armstrong number')
else:
    print(f'{num} is not Armstrong number')