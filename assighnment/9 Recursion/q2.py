# n = 153
# temp = n 
# count = 3
# sum = 0
# while(temp > 0):
#     d = temp % 10
#     sum += d ** count
#     temp //=10
# print(sum)

def checkArmstrong(n,count,temp,sum=0):
    if(temp <= 0):
        if(sum == n):
            # print(f'{n} is an Armstrong Number')
            return True
        else:
            # print(f'{n} is not an Armstrong Number')
            return False
    d = temp % 10 
    sum += d ** count 
    return checkArmstrong(n,count,temp//10,sum)

n = int(input('enter number: '))
count = len(str(n))
temp = n 
res = checkArmstrong(n,count,temp)
if(res):
    print(f'{n} is an Armstrong Number')
else:
    print(f'{n} is not an Armstrong Number')