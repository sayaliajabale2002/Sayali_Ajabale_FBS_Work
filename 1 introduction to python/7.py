# ax2+bx+c=0

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

value = ((b**2)-(4*a*c))**0.5
x1 = (-b+value)/(2*a)
x2 = (-b-value)/(2*a)

print(f'Roots are {x1} and {x2}')