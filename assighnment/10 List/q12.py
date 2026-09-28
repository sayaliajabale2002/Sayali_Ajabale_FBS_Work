def createList():
    li = []
    n = int(input('enter length of list: '))
    for i in range(n):
        el = int(input(f'enter element {i}: '))
        li.append(el)
    return li 

def cubeList(li):
    cube_li = []
    for i in li:
        cube_li.append(i**3)
    return cube_li

def squareList(li):
    squ_li = []
    for i in li:
        squ_li.append(i**2)
    return squ_li

new_list = createList()
cube_list = cubeList(new_list)
squ_list = squareList(new_list)

print(new_list)
print(cube_list)
print(squ_list)