n = int(input('enter number: '))

for i in range(1,n+1):
    salary = int(input(f'enter salary of emp {i}: '))
    if(salary <= 20000):
        da = (20000/100)*10
        ta = (20000/100)*12
        hra = (20000/100)*15
        total_salary = salary + da + ta + hra
    else:
        da = (20000/100)*15
        ta = (20000/100)*18
        hra = (20000/100)*20
        total_salary = salary + da + ta + hra

    print(f'total salary for emp {i} is {total_salary}')
    