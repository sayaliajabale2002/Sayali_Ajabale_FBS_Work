def createList():
    li = []
    n = int(input('enter length of list:'))
    for i in range(n):
        el = int(input(f'enter element {i}:'))
        li.append(el)
    return li 

def squareList(li):
    squli = []
    for i in range(len(li)):
        squli.append(li[i]**2)
    return squli

def cubeList(li):
    cubeli = []
    for i in range(len(li)):
        cubeli.append(li[i]**3)
    return cubeli

li = createList()
print(li)
squli = squareList(li)
cubeli = cubeList(li)
print(squli)
print(cubeli)