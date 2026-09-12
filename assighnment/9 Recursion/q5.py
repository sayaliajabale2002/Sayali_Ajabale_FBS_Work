n = 5
# fact = 1
# while(n>0):
#     fact *= n
#     n -= 1
# print(fact)

def Factorial(n):
    if(n==1):
        return 1
    else:
        return n * Factorial(n-1)
n=int(input('enter number: '))
print(Factorial(n))