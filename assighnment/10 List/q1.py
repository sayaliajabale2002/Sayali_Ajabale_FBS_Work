# from functools import reduce

li = [10,20,40,30,60,50]

# res = reduce(lambda x,y : x+y , li)
# print('sum is',res)

def sumList(li):
    sum = 0
    for i in li:
        sum += i
    return sum

res = sumList(li)
print('sum is',res)