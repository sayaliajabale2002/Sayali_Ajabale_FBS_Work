num = int(input('enter number: '))
temp = num
sum = 0
# fact = 1

while(temp > 0):
    d = temp % 10 
    fact = 1
    for i in range (1,d+1):
        fact *= i 
    # print(fact)
    sum += fact
    # print(sum) 
    temp //= 10 

if(sum == num):
    print(f'{num} is strong number')
else: 
    print(f'{num} is not strong number')