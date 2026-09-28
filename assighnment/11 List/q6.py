li1 = [10,20,30,40,50]
li2 = [30,40,50,60,70,80]

def unionList(li1,li2):
    newli=[]

    for i in range(len(li1)):
        if(li1[i] not in newli):
            newli.append(li1[i])

    for j in range(len(li2)):
        if(li2[j] not in newli):
            newli.append(li2[j])
            
    return newli

res = unionList(li1,li2)
print(res)