a = int(input('enter value of a: '))

sum = 0
print("S = ",end=" ")
for i in range(1,11):
    sum += (a**i)/i
    print(f'(a**{i})/{i} + ',end=" ")

print()
print(sum)