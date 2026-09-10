def factorial(num):
    if(num == 0):
        return 1
    fact = 1
    for i in range(1,num+1):
        fact *= i 
    # print("fact =",fact)
    return fact 

def sum(terms):
    sum = 0 
    for i in range(1,terms+1):
        sum += factorial(i)
    # print("sum",sum)
    return sum 

t = int(input("enter number of terms: "))
res = sum(t)
print(f'sum of {t} numbers is {res}')