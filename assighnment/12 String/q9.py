s = 'Python is a great programming language.'
alp = 0
words = 0
for i in s:
    if(i.isalpha()):
        alp += 1

    if(i.isspace()):
        words += 1

print('total words are ',words+1)
print('total characters are ',alp)

