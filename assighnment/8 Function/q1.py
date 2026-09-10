def areaOfRectangle(length, breadth):
    area = length * breadth
    return area

l = int(input("enter length of rectangle: "))
b = int(input("enter breadth of rectangle: "))

res = areaOfRectangle(l,b)
print(f'area of rectangle is {res}')