li = [1,2,3,4,5,6]

def cubeList(li):
    new_list = []
    for i in range(len(li)):
        el = li[i] ** 3
        new_list.append(el)
    return new_list

res = cubeList(li)
print(res)