li = [10,20,40,30,60,50]

# highest = max(li)
# lowest = min(li)

def maxminList(li):
    highest = li[0]
    lowest = li[0]

    for i in range(1,len(li)):
        if(highest < li[i]):
            highest = li[i]
        if(lowest > li[i]):
            lowest = li[i]

    print('maximum number is', highest)
    print('minimum number is', lowest)

maxminList(li)