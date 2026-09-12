def Power(m,n):
    if(n==0):
        return 1
    else:
        return m * Power(m,n-1)

m = int(input("enter number: "))
n = int(input("enter power of number: "))
res = Power(m,n)
print(res)