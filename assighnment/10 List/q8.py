li_1 = [10,20,30,40,50]
li_2 = []

def duplicate_list(li_1,li_2):
    for i in li_1:
        li_2.append(i)

duplicate_list(li_1,li_2)
print(li_1)
li_2.append(60)
print(li_2)
