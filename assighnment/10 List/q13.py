li = [1,2,3,4,5,6,7,8,9]

def removeEven(li):
    new_li = []
    for i in li:
        if(i%2 != 0):
            new_li.append(i)
    return new_li

res = removeEven(li)
print(res)