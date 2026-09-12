# n = 123
# temp = n
# rev = 0
# while(temp>0):
#     d = temp % 10
#     rev = rev*10 + d
#     temp //= 10
# print(rev)

def Reverse(n,rev=0):
    if(n<=0):
        # print(f"reverse is {rev}")
        return rev
    d = n%10
    rev = rev * 10 + d
    return Reverse(n//10,rev)

n = int(input('enter number: '))
res = Reverse(n)
print(res)