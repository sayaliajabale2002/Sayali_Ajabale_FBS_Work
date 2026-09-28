li1 = [10,30,50,70]
li2 = [20,40,60,80]

def mergeList(li1,li2):
    # new_list = []
    new_list = li1 + li2
    # for i in li1:
    #     new_list.append(i)
    # for j in li2:
    #     new_list.append(j)
    return new_list

def sort(li):
    n = len(li)
    for i in range(1,n):
        for j in range(n-i):
            if(li[j] > li[j+1]):
                li[j],li[j+1] = li[j+1],li[j]


li = mergeList(li1,li2)
print('merge list is',li)
sort(li)
print('sorted list is',li)