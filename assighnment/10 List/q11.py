li = [10,20,40,30,60,50]
m = int(input('enter number: '))
n = int(input('enter number: '))

def divisibleNumber(li,m,n):
    new_li = []
    for i in li:
        if(i%m == 0 and i%n ==0):
            new_li.append(i)
    return new_li

res = divisibleNumber(li,m,n)
print(res)