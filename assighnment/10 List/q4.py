li = [10,20,30,40,50,70]

def reverseList(li):
    i = 0
    j = len(li)-1
    while(i<j):
        # temp = li[i]
        # li[i] = li[j]
        # li[j] = temp 
        li[i],li[j] = li[j],li[i]
        i += 1
        j -= 1
    return (li)

res = reverseList(li)
print(res)

