def Reverse(n,rev=0):
    if(n<=0):
        # print(rev)
        return rev
    d = n % 10
    rev = rev * 10 + d
    return Reverse(n//10,rev)

n = int(input('enter number: '))
res=Reverse(n)
print(res)