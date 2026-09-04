k=7
for i in range(5):
    for j in range(i+1):
        print(j+1,end=" ")

    for j in range(k):
        print(" ",end=" ")
    k -= 2

    for j in range(i+1):
        if(i==4 and j==0):
            continue
        else:
            print(i-j+1,end=" ")

    print()

print()

# for i in range(0,5):
#     for j in range(i+1):
#         if(i==4 and j==0):
#             continue
#         else:
#             print(i-j+1,end=" ")
#     print()