p1 = int(input('enter price of product 1: '))
p2 = int(input('enter price of product 2: '))
p3 = int(input('enter price of product 3: '))
p4 = int(input('enter price of product 4: '))
p5 = int(input('enter price of product 5: '))

cost = p1 + p2 + p3 + p4 + p5 

gst = (cost*18)/100
# print(gst)

total_cost = cost + gst 

print(f'Total cost is by adding 18% GST is {total_cost}')