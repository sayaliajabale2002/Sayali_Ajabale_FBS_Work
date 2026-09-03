passengers = int(input('enter number of passengers: '))
ticket_cost = float(input('enter per ticket cost: '))

total_cost = 0

for i in range(1,passengers+1):
    print(f'Enter details of passanger {i}: ')
    age= int(input(f'enter age of person: '))
    if(age<=12):
        discount = (ticket_cost*30)/100
        cost = ticket_cost - discount
    elif(age>=59):
        discount = (ticket_cost*50)/100
        cost = ticket_cost - discount
    else:
        cost = ticket_cost
        
    total_cost += cost

print('total cost is', total_cost)