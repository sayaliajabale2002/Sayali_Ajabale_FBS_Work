P = int(input("Enter principle amount: "))
R = int(input("Enter Rate: "))
T = int(input("Enter time: "))

CI = (P*(1+(R/100))**T)-P
print(f"Compound Interest = {CI}")