li1 = [10,20,30,40,50]
li2 = [30,40,50,60,70]

def intersectionList(li1,li2):
    newli = []
    for i in li1:
        for j in li2:
            if(i == j):
                newli.append(j)
    return newli

res = intersectionList(li1,li2)
print(res)