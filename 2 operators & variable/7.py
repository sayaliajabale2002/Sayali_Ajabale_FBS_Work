num = int(input("enter 3 digit number: "))
n = num
sum = 0

while (num>0):
    digit = num % 10 
    sum += digit
    num //= 10 

print(f"sum of 3 digit number {n} is {sum}")