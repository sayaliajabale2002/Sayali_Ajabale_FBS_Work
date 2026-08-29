x = int(input('enter number: '))
y = int(input('enter number: '))

print(f'before swaping x={x} & y={y}')

# x,y = y,x

x = x+y  # 10+20 30
y = x-y  
x = x-y

print(f'after swaping x={x} & y={y}')