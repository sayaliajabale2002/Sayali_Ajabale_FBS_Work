unit = int(input('Enter total electricity unit charge: '))

charges = 0 

if(unit <= 50):
    charges = unit * 0.50
elif(unit <= 150):
    charges = unit * 0.75
elif(unit <= 250):
    charges = unit * 1.20
else:
    charges = unit * 1.50

print(f'electricity bill = {charges}')
    