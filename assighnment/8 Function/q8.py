def reverse(n):
    rev = 0
    while(n>0):
        d = n % 10 
        rev = rev * 10 + d 
        n //= 10 
    return rev 

n = int(input('enter number: '))
res = reverse(n)
print(res)