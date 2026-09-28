li = [10,20,40,30,60,50]

def secondLargest(li):
    max_1 = li[0]
    max_2 = 0
    for i in range(1,len(li)):
        if(max_1 < li[i]):
            max_2 = max_1
            max_1 = li[i]
        elif(max_2 < li[i]):
            max_2 = li[i]
    print('first largest number:',max_1)
    print('second largest number:',max_2)

secondLargest(li)