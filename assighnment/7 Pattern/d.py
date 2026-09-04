for i in range(5):
    for j in range(4-i):
        print(" ",end=" ")

    for j in range(i+1):
        print(i+j+1,end=" ")

    for j in range(i):
        print(i*2-j,end=" ")
    
    print()

