s = 'Python is a great programming language.'
count = 0
# print(len(s))
for i in s:
    if(i.islower()):
        count += 1

print('total lower characters are ', count)