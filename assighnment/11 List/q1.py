li = [1,2,3,4,5,6,7,8,9,10]

def oddevenList(li):
    odd_list = []
    even_list = []
    for i in li:
        if(i%2==0):
            even_list.append(i)
        else:
            odd_list.append(i)
    print('odd list is',odd_list)
    print('even list is',even_list)

print('original list is',li)
oddevenList(li)