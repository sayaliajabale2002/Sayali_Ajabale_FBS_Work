li = [10,20,40,40,30,20,60,50,40,20,40]

def removeDuplicate(li):
    new_list = []
    for i in li:
        if(i not in new_list):
            new_list.append(i)
    return new_list

remove_duplicate = removeDuplicate(li)
print(remove_duplicate)