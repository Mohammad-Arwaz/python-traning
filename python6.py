'''a = 10
b = 24
if a > b:
    print('this is  true')
    print('please try again with some other var')
else:
    print('this is not true')'''

#x = int(input('please inter any number:'))
'''
if x < 100:
    print('great work')
    print('your promotion is confirmed')
    print(f'you enter x is {x}')         
else:
    print('you are not doing great work')
    print('please do hard work')
    print('nighter i fire you from company')'''


'''x = int(input('please inter any number:'))

if x % 2 == 0:
    print('number is even')
    print(f'you enter x {x}')
    print('good job')
else:
    print('number is odd')
    print(f'you enter x {x}')
    print('bad job try again')'''


#leap year program

year = int(input('enter the year:'))

if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print(year,'is a leap year')
else:
    print(year,'is not a leap year')
