# def sumofDigits(n,sum=0):
#     if(n<=0):
#         print(sum)
#         return
#     d = n % 10
#     sum += d 
#     sumofDigits(n//10,sum)

def sumofDigits(n):
    if(n==0):
        return 0
    return n%10 + sumofDigits(n//10)

n = int(input("enter number: "))
res = sumofDigits(n)
print(res)