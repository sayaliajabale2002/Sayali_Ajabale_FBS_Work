li = [[6,7,8],[3,4,5],[9,10]]

def secondsubelementsort(li):
    n = len(li)
    for i in range(1,n):
        for j in range(n-i):
            if(li[j][1]> li[j+1][1]):
                li[j],li[j+1] = li[j+1],li[j]

secondsubelementsort(li)
print(li)
