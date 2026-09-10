def leapYear(year):
    if((year%4==0 and year%100!=0) or year%400==0):
        return True
    else:
        return False

year = int(input('enter year: '))
res = leapYear(year)

if(res):
    print(f'{year} is leap year')
else:
    print(f'{year} is not leap year')

