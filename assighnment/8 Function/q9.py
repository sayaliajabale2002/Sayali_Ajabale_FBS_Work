def reverse(n):
    rev = 0
    while(n>0):
        d = n % 10 
        rev = rev * 10 + d 
        n //= 10 
    return rev

def pallindrom(n):
    rev = reverse(n)
    if(rev == n):
        return True
    else:
        return False

n = int(input('enter number: '))
res = pallindrom(n)
print(res)

