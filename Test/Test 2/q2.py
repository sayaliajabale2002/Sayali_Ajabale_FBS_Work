num = int(input('enter 3 digit number: '))

temp = num
count = 0
while(temp>0):
    temp //= 10
    count += 1
# print(count)

if(count == 3):
    temp = num
    d3 = temp%10
    temp //= 10
    d2 = temp%10
    temp //=10
    d1 = temp%10
    temp //= 10
    # print(d1,d2,d3)
    if(d1==(d2*2) and d1==(d3//2)):
        print("Yes, you have done it")
    else:
        print("Please try next time")
else:
    print("enter 3 digit number")