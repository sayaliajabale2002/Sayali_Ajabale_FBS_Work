for i in range(5):
    for j in range(5):
        if(i%2==0):
            if(j%2==0):
                print("1",end=" ")
            else:
                print("0",end=" ")
        else:
            if(j%2==0):
                print("0",end=" ")
            else:
                print("1",end=" ")
    print(" ")