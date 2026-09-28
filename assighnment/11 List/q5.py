def lengthSort(li):
    for i in range(len(li)):
        min_idx = i

        if(type(li[i]) == int):
            min_len = len(str(li[i]))
        else:
            min_len = len(li[i])

        for j in range(i,len(li)):
            if(type(li[j])==int):
                if(len(str(li[j])) < min_len):
                    min_idx = j 
            else:
                if(len(li[j]) < min_len):
                    min_idx = j 

        li[i],li[min_idx] = li[min_idx],li[i]


li = [12,'kiwi','pot','beautiful',10,3456]
print(li)
lengthSort(li)
print(li)