start = int(input('enter starting number of range: '))
end = int(input('enter ending number of range: '))

for i in range(start, end+1):
    if i%7==0 and i%5==0:
        print(i)