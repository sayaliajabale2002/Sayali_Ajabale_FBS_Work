for i in range(5):
    for j in range(4-i):
        print(" ",end=" ")

    for j in range(i+1):
        if(j==0 or i==4 or i==j):
            print(j+1,end="   ")
        else:
            print(" ",end="   ")
    
    print()