def snakeLadder():
    st = 100 
    ladder = []
    for i in range(10):
        if(i%2==0):
            for j in range(10):
                print(st,end=" ")
                st -= 1
        if(i%2 != 0):
            for j in range(9,0,-2):
                if(i == 9):
                    print(st-j,end="  ")
                else: 
                    print(st-j,end=" ")
                st -= 1    
            for j in range(1,10,2):
                if(i == 9):
                    print(st+j,end="  ")
                else: 
                    print(st+j,end=" ")
                st -= 1
        print()

snakeLadder()