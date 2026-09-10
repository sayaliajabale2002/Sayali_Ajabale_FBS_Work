# length of number
def num_len(n):
    count = 0
    while(n>0):
        count += 1
        n //= 10 
    return count

# giving multiplication 
def power(n,length):
    return n ** length

#giving sum of that number
def sum(n):
    sum = 0
    count = num_len(n)
    while(n>0):
        d = n % 10 
        sum += power(d,count)
        n //= 10 
    # print(sum)
    return sum 

#giving bool value to check number
def checkArmstrong(n):
    armstrong = sum(n)
    if(armstrong == n):
        return True
    else:
        return False

n = int(input('enter number: '))
res = checkArmstrong(n)
print(res)