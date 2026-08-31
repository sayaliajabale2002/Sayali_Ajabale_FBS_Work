x = int(input('enter side of triangle (x): '))
y = int(input('enter side of triangle (y): '))
z = int(input('enter side of triangle (z): '))


if(x==y and y==z):
    print('Equilateral Triangle')
elif(x==y or x==z or y==z):
    print('Isosceles Triangle')
else:
    print('Scalene Triangle')