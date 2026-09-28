s1 = input('enter string 1: ')
s2 = input('enter string 2: ')

if(len(s1) == len(s2)):
    for i in s1:
        if(i not in s2):
            print(f"{s1} and {s2} Not Anagrams")
            break
    else:
        print(f"{s1} and {s2} are Anagrams")
else:
    print(f"{s1} and {s2} Not Anagrams")