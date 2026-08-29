# notes: 500,200,100,50,20,10

num = int(input("enter any number: "))
n_500 = num // 500
print(n_500)
num = num%500

n_200 = num // 200
print(n_200)
num = num%200

n_100 = num // 100
print(n_100)
num = num%100

n_50 = num // 50 
print(n_50)
num = num%50

n_20 = num // 20
print(n_20)
num = num%20

n_10 = num // 10
print(n_10)
num = num%10 

total = n_500 + n_200 + n_100 + n_50 + n_20 + n_10 

print(f"total notes required = {total}, remaining = {num}")