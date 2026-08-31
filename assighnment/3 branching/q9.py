hindi = int(input("enter your marks in hindi subject: "))
marathi = int(input("enter your marks in marathi subject: "))
math = int(input("enter your marks in math subject: "))
science = int(input("enter your marks in science subject: "))
english = int(input("enter your marks in english subject: "))

total_marks = (hindi + marathi + math + science + english)/5


if(total_marks >= 90):
    print('First class')
elif(total_marks >= 80):
    print('Second class')
elif(total_marks >= 70):
    print('Third class')
elif(total_marks >= 60):
    print('Fourth class')
else:
    print('Improve your marks')