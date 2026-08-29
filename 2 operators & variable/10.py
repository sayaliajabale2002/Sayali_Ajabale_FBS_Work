num = int(input("enter 3 digit number: "))
rev=0
while(num>0):
    reminder = num%10
    rev = rev*10 + reminder
    num //=10

print(f"reverse = {rev}")