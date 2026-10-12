def factors(n):
    for i in range(1,n):
        if(n%i==0):
            print(i,end=", ")
    print(n)

n = int(input('enter number: '))
factors(n)