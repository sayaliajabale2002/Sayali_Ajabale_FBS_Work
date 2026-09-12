# n=3
# i=1
# sum = 0
# while(i<=n):
#     fact = 1
#     for j in range(1,i+1):
#         fact *= j
#     sum += fact
#     i += 1
# print(sum)

def sumofFactorial(n,sum=0,fact = 1,count=1):
    if(n <=0):
        # print("0")
        return 0
    if(n+1==count):
        # print(f'sum is {sum}')
        return sum
    fact *= count
    sum += fact
    count += 1
    return sumofFactorial(n,sum,fact,count)

n = int(input('enter number of terms: '))
sum = sumofFactorial(n)
print(f'sum is {sum}')