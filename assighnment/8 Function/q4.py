def odd(num):
    if(num%2 != 0):
        return True

def sum(terms):
    num_odd = False
    sum = 0
    for i in range(1,terms):
        num_odd = odd(i)
        if(num_odd):
            print(i)
            sum += i
    return sum 

t = int(input("enter number of terms: "))
res = sum(t)
print(f'sum of odd numbers from 1 to {t} is {res}')