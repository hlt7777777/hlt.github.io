
# name = input('please input your name:')
print('name')

print()

print('dsdf dsdfsf dfsf\ndfsf ')

print('hello')
print('world')
first_name = 'hello'
last_name = 'world'
print('my ' + first_name.capitalize() + ' ' + last_name.capitalize())

print( first_name + last_name )
output = 'my {0}, {1}'.format(first_name, last_name)
print(output)

output1 = f'it is {first_name} - {last_name}'
print(str(9969).replace('6', '9', 1))

a = [[1,2,3],[4,5,6],[7,8,9]]

from datetime import datetime,timedelta

today = datetime.now()
days = timedelta(days = 1)

yesterday = today - days 
print(today,yesterday)

one_week = timedelta(weeks=1)
last_week = today - one_week
print(last_week)

birthday = input('input your date(dd/mm/yyyy)')
birthday_day = datetime.strptime(birthday, '%d/%m/%Y')
print(str(birthday_day))