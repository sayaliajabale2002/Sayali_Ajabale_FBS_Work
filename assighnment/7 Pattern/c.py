for i in range(5):
    for j in range(i+1):
        if(i == 4):
            print(j+1,end=" ")
        elif(j==0):
            print(j+1,end=" ")
        elif(i==j):
            print(j+1,end=" ")
        else:
            print(" ",end=" ")
    print()