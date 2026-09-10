def fibonacci(term):
    if(term<=0):
        print('enter number greater than 0')
    a = 1
    b = 1
    if(n == 1):
        print(a)
        return
    elif(n== 2):
        print(f'{a},{b}')
        return

    print(f'{a}, {b}',end=" ")
    for i in range(2,n):
        temp = a + b 
        print(f',{temp}',end=" ")
        a = b 
        b = temp
    return 

n = int(input("enter number of terms: "))
fibonacci(n)