n = int(input('enter number of elements: '))

def createList(n):
    new_list = []
    for i in range(n):
        el = int(input(f'enter element {i+1}: '))
        new_list.append(el)
    return new_list

def oddElement(li):
    odd_list = []
    for i in li:
        if(i%2 != 0):
            odd_list.append(i)
    return odd_list

def evenElement(li):
    even_list = []
    for i in li:
        if(i%2 == 0):
            even_list.append(i)
    return even_list

li = createList(n)
print('list is',li)
even = evenElement(li)
odd = oddElement(li)
print('even list is',even)
print('odd list is',odd)

