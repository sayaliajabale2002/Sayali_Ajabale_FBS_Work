age_1 = int(input('enter age of person 1: '))
amount_1 = float(input('enter ticket amount for person 1: '))
age_2 = int(input('enter age of person 2: '))
amount_2 = float(input('enter ticket amount for person 2: '))
age_3 = int(input('enter age of person 3: '))
amount_3 = float(input('enter ticket amount for person 3: '))
age_4 = int(input('enter age of person 4: '))
amount_4 = float(input('enter ticket amount for person 4: '))
age_5 = int(input('enter age of person 5: '))
amount_5 = float(input('enter ticket amount for person 5: '))

if(age_1 < 12):
    discount_1 = (amount_1 * 30)/100
    amount_1 -= discount_1
elif(age_1 > 59):
    discount_1 = (amount_1 * 50)/100
    amount_1 -= discount_1

if(age_2 < 12):
    discount_2 = (amount_2 * 30)/100
    amount_2 -= discount_2
elif(age_2 > 59):
    discount_2 = (amount_2 * 50)/100
    amount_2 -= discount_2

if(age_3 < 12):
    discount_3 = (amount_3 * 30)/100
    amount_3 -= discount_3
elif(age_3 > 59):
    discount_3 = (amount_3 * 50)/100
    amount_3 -= discount_3

if(age_4 < 12):
    discount_4 = (amount_4 * 30)/100
    amount_4 -= discount_4
elif(age_4 > 59):
    discount_4 = (amount_4 * 50)/100
    amount_4 -= discount_4

if(age_5 < 12):
    discount_5 = (amount_5 * 30)/100
    amount_5 -= discount_5
elif(age_5 > 59):
    discount_5 = (amount_5 * 50)/100
    amount_5 -= discount_5

total_amount = amount_1 + amount_2 + amount_3 + amount_4 + amount_5

print(f'total amount is {total_amount}')