def sum(terms):
    sum = 0
    for i in range(1,terms+1):
        sum += i 
    return sum 

n = int(input("enter nth term: "))
res = sum(n)
print(f'sum of {n} numbers is {res}')