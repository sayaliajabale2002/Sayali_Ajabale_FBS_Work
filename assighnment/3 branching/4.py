x = int(input('enter side of triangle (x): '))
y = int(input('enter side of triangle (y): '))
z = int(input('enter side of triangle (z): '))

if(x+y > z and x+z > y and y+z > x):
    print('Valid triangle')
else:
    print('invalid triangle')