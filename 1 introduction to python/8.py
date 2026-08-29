days = int(input("Enter days: "))

# for standard year 365 days
# for leap year 366 days

year = days // 365
days = days % 365 
weeks = days // 7
days = days % 7

print(f'In {days} days year={year}, weeks={weeks}, days={days}')
# print(11*365 + 24*7 + 5)