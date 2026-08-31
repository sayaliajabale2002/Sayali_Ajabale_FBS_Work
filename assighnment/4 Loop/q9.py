start = int(input('enter starting number of range: '))
end = int(input('enter ending number of range: '))

num = int(input('enter number by which range will divisible: '))

for i in range (start, end+1):
    if(i%num == 0):
        print(i)