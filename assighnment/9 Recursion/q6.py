def Fibonacci(n):
    if n==1 or n==2: 
        return 1
    return Fibonacci(n-1)+Fibonacci(n-2)

n = int(input('enter number of terms: '))
for i in range(1,n+1):
    print(Fibonacci(i),end=" ,")