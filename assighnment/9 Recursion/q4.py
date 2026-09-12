def sumofSeries(n):
    if(n<=0):
        return 0
    else:
        return n + sumofSeries(n-1)

term = int(input('enter number of terms: '))
res = sumofSeries(term)
print(f'sum of {term} terms is {res}')