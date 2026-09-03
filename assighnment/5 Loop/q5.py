# st = int(input('enter starting number : '))
# end = int(input('enter ending number : '))

for i in range(1,100+1):
    # Prime = True
    if(i>1):
        for j in range(2,i):
            if(i%j == 0):
                # Prime = False
                break
        # if(Prime):
        #     print(i,end=" ,")
        else:
            print(i,end=" ,")



