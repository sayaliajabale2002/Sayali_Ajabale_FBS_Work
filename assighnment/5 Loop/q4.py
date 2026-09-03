st = int(input('enter starting of the range of Armstrong number: '))
end = int(input('enter ending of the range of Armstrong number: '))

for i in range(st,end+1):
    original = i
    temp = i
    count = 0
    while(temp>0):
        temp //= 10
        count+=1

    num = i
    sum = 0
    while(num>0):
        digit = num % 10
        num //= 10
        sum += digit**count

    if(original == sum):
        print(sum)