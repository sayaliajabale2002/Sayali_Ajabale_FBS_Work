x = int(input('enter angle of triangle (x): '))
y = int(input('enter angle of triangle (y): '))
z = int(input('enter angle of triangle (z): '))

angles = x+y+z

if(angles == 180):
    print('Valid triangle')
else:
    print('invalid triangle')