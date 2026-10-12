def factorial(n,fact=1):
    if(n<=1):
        return fact
    else:
        return factorial(n-1,fact*n)

res = factorial(5)
print(res)
