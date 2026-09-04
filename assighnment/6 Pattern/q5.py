k=1
for i in range(5):
    for j in range(4-i):
        print(" ",end=" ")
    
    for j in range(k):
        print("*",end=" ")
    k += 2

    # for j in range(i):
    #     print("*",end=" ")
    print()