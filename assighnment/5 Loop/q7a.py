n = int(input('enter first n numbers : '))

sum = 0
for i in range(1,n+1):
    fact = 1
    for j in range(1,i+1):
        fact *= j
        # print(fact)
    # print(fact)
    sum += fact

print(f'sum of factorial for {n} numbers is : {sum}')