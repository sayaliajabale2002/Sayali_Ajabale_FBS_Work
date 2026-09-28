li = [10,20,40,30,20,60,50,40,20]
target = int(input('enter element: '))

def removeElement(li,target):
    new_li = []
    for i in li:
        if(i != target):
            new_li.append(i)
    return new_li

res = removeElement(li,target)
print(res)
