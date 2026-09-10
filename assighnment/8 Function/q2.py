def areaOfCircle(radius):
    area = 3.14 * radius * radius
    return area

r = int(input("enter radius of circle: "))
res = areaOfCircle(r)
print(f'area of circle is {res}')