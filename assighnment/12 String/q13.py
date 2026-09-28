s = 'Python is a great programming language 2345.'
count_num = 0
count_letter = 0
for i in s: 
    if(i.isalpha()):
        count_letter += 1
    elif(i.isnumeric()):
        count_num += 1

print(f'total digits are : {count_num}')
print(f'total characters are : {count_letter}')