area = int(input('Area of 1 wall: '))

cost_interior = float(input('Cost for painting 1 interior wall: '))
cost_exterior = float(input('Cost for painting 1 exterior wall: '))

total_interior = 7 * cost_interior
total_exterior = 7 * cost_exterior

total_cost = total_interior + total_exterior

print("Total cost is: ",total_cost)