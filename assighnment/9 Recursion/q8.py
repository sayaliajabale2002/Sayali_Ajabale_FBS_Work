# i =2
# n=10
# while(i<= (n//2+1)):
#     if(n%i == 0):
#         print("not prime")
#         break
#     i += 1
# print("prime")

def Prime(n,i=2):
    if(n<=1):
        return True
    elif(n==2):
        return False
    elif(n%i == 0):
        return True
    elif(i > ((n//2)+1)):
        return False
    i += 1
    Prime(n,i)

n = int(input('enter number:'))
if(Prime(n)):
    print("Not Prime")
else:
    print("Prime")
        