n=int(input('enter number of terms: '))
count = 0
for i in range(1,n+1):
    if(i%2 != 0):
        print('+',end=" ")
    elif(i%2 == 0):
        print('-',end=" ")

    print(f"x{i}/{i+count}",end=" ")
    count += 1