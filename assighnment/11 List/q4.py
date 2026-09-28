li = [9,6,2,4,5]

def bubbleSort(li):
    n=len(li)
    for i in range(1,n):
        for j in range(n-i):
            if(li[j] > li[j+1]):
                li[j],li[j+1] = li[j+1],li[j]

bubbleSort(li)
print(li)
print('second largest number is',li[-2])