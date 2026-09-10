def Power(num):
    pow = num ** num 
    return pow 

def sum(terms):
    sum = 0
    for i in range(1,terms+1):
        sum += Power(i)
    return sum 

t = int(input("enter number of terms: "))
res = sum(t)
print(f'sum of {t} numbers is {res}')