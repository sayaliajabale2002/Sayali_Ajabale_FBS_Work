def pattern(n):
    for i in range(n):
        if i == 0 or i == n-1:
            print("*" * ((n-1)*2))
        else:
            print(" " * (((n-1)*2) - i * 2) + "*")

n = int(input("enter number: "))
pattern(n)
# n = 12
