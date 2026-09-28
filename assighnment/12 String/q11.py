s = 'Python is a great programming language.'
new_s = ""
for i in s:
    if(i.isspace()):
        i = "-"
        new_s += i 
    else:
        new_s += i
print(new_s)

