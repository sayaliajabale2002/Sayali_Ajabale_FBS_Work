def prime(num):
    if(num < 2):
        return False

    if(num%2 == 0):
        return False
    else:
        for i in range(3,(num//2)+2):
            if(num%i == 0):
                return False 
        return True


def sum(terms):
    num_prime = False
    sum = 0
    for i in range(1,terms):
        num_prime = prime(i)
        if(num_prime):
            # print(i)
            sum += i
    return sum 

t = int(input("enter number of terms: "))
res = sum(t)
print(f'sum of prime numbers from 1 to {t} is {res}')