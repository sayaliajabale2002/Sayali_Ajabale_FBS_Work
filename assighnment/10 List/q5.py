def Search(li,n):
    count = 0
    for i in range(len(li)):
        if(n == li[i]):
            count += 1
    return count

li = [10,20,40,30,20,60,50,40,20]
num = int(input('enter number: '))

res = Search(li,num)
if(res > 0):
    print(f'{num} is present {res} time in list')
else:
    print(f'{num} not present')