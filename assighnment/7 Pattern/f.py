for i in range (5):
    for j in range(5-i):
        if(j==0 or i==0 or i+j==4):
            print(i+j+1,end=" ")
        else:
            print(" ",end=" ")
        
    print()