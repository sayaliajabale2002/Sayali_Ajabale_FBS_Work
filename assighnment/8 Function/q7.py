def sumofDigits(n):
    sum = 0
    while(n>0):
        d = n % 10
        sum += d
        n //= 10 
    return sum 

n = int(input("enter number: "))
res = sumofDigits(n)
print(res)