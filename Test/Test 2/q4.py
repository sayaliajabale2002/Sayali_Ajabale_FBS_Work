cost = int(input('enter cost of 1 meter square: '))
length= int(input('enter length of wall: '))
breadth = int(input('enter breadth of wall: '))

areaofWall = length*breadth
total_areaofWall = 4 * areaofWall

total_cost = total_areaofWall * cost

print(f'total cost = {total_cost} rupees')