sp = int(input('enter selling price: '))
cp = int(input('enter cost price: '))

if(sp > cp):
    profit = sp - cp 
    print(f'profit = {profit}')
else:
    loss = cp - sp
    print(f'loss = {loss}')