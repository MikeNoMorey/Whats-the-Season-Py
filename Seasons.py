#Season Generator v1.0
#Created by Mike Morey, thanks for looking!

print('Please input the month?')
input_month = input()
print('Please input the date?')
input_day = int(input())
print()

if input_month == 'January' and input_day > 0 and input_day <= 31:
    print('Brr.. it\'s Winter \n')
elif input_month == 'February' and input_day > 0 and input_day <= 29:
    print('Brr.. it\'s Winter \n')
elif input_month == 'March':
    if input_day > 0 and input_day <= 19:
        print('Brr.. it\'s Winter \n')
    elif input_day > 19 and input_day <= 31:
        print('Hooray it\'s Spring! \n')
    else:
        print('Invalid')
        
        
elif input_month == 'April' and input_day > 0 and input_day <= 31:
    print('Hooray it\'s Spring! \n')
elif input_month == 'May' and input_day > 0 and input_day <= 31:
    print('Hooray it\'s Spring! \n')
elif input_month == 'June':
    if input_day > 0 and input_day <= 20:
        print('Hooray it\'s Spring! \n')
    elif input_day > 20 and input_day <= 31:
        print('It\'s Summer, Drink some watah! \n')
    else:
        print('Invalid')
        
        
elif input_month == 'July' and input_day > 0 and input_day <= 31:
    print('It\'s Summer, Drink some watah! \n')
elif input_month == 'August' and input_day > 0 and input_day <= 31:
    print('It\'s Summer, Drink some watah! \n')
elif input_month == 'September':
    if input_day > 0 and input_day <= 21:
        print('It\'s Summer, Drink some watah! \n')
    elif input_day > 21 and input_day <= 30:
        print('Finally it\'s Autumn again. \n')
    else:
        print('Invalid')
        
        
elif input_month == 'October' and input_day > 0 and input_day <= 31:
    print('Finally it\'s Autumn again. \n')
elif input_month == 'November' and input_day > 0 and input_day <= 31:
    print('Finally it\'s Autumn again. \n')
elif input_month == 'December':
    if input_day > 0 and input_day <= 20:
        print('Finally it\'s Autumn again. \n')
    elif input_day > 20 and input_day <= 31:
        print('Brr.. it\'s Winter \n')
    else:
        print('Invalid')
else:
    print('Invalid')