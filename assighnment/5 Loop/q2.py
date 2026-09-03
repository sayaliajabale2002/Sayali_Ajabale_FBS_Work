students = int(input("enter number of students: "))

for i in range(1,students+1):
    print(f'Enter marks of Student {i}')
    sub1 = int(input("marks obtain in subject 1: "))
    sub2 = int(input("marks obtain in subject 2: "))
    sub3 = int(input("marks obtain in subject 3: "))
    sub4 = int(input("marks obtain in subject 4: "))
    sub5 = int(input("marks obtain in subject 5: "))
    percentage = (sub1+sub2+sub3+sub4+sub5)*100/500
    print(f'percentage of student {i} = {percentage}\n')