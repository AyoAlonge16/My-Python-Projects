year = input('year you want to check: ')
year_num = int(year)

if year_num % 4 == 0:
    print(year_num, 'is a Leap Year')
else:
    print(year_num, 'is not a Leap year')


