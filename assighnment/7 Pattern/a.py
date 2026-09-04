k=1
for i in range(5):
    for j in range(4-i):
        print(" ",end=" ")

    for j in range(1):
        print("*",end=" ")

    if(i>=1):
        for j in range(k):
            print(" ",end=" ")
        k += 2

    if(i>=1):
        for j in range(1):
            print("*",end=" ")
    print()


k=7
for i in range(5):
    for j in range(i):
        print(" ",end=" ")

    for j in range(1):
        print("*",end=" ")

    # if(i<=5):
    for j in range(k):
        print(" ",end=" ")
    k -= 2

    if(i<4):
        for j in range(1):
            print("*",end=" ")
    print()