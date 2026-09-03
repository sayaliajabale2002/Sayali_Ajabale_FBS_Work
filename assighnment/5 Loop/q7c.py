n = int(input('enter first n numbers : '))

sum = 0
for i in range(n):
    sum += 2**(i)
print(f'sum of a geometric series from 1 to {n} where the common ratio is 2 = {sum}')