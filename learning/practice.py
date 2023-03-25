
# # name = input('please input your name:')
# print('name')

# print()

# print('dsdf dsdfsf dfsf\ndfsf ')

# print('hello')
# print('world')
# first_name = 'hello'
# last_name = 'world'
# print('my ' + first_name.capitalize() + ' ' + last_name.capitalize())

# print( first_name + last_name )
# output = 'my {0}, {1}'.format(first_name, last_name)
# print(output)

# output1 = f'it is {first_name} - {last_name}'
# print(str(9969).replace('6', '9', 1))

# a = [[1,2,3],[4,5,6],[7,8,9]]

# from datetime import datetime,timedelta

# today = datetime.now()
# days = timedelta(days = 1)

# yesterday = today - days 
# print(today,yesterday)

# one_week = timedelta(weeks=1)
# last_week = today - one_week
# print(last_week)

# birthday = input('input your date(dd/mm/yyyy)')
# birthday_day = datetime.strptime(birthday, '%d/%m/%Y')
# print(str(birthday_day))

# x = 420 
# y = 0 

# try:
#     print(x / y)
# except ZeroDivisionError as e:
#     print('zero')
# else:
#     print('ture')
# finally:
#     print('finally')

# princ = 0.8
# if princ >= 1.0:
#     tax = 0.7
# else:
#     tax = 1

# print(tax)

# a = 1
# if a == 1:
#     print(12)
# elif a == 2:
#     print(17)

def f(name, force_uppercase = True):
    if force_uppercase:
        first_name = name[0:1].upper()
    else:
        first_name = name[0:1]
    return first_name


# init_name = input('your name is:')
final = f('init_name')
print(final)

class Solution(object):
    def largestTimeFromDigits(self, A):
        ans = -1
        for h1, h2, m1, m2 in itertools.permutations(A):
            hours = 10 * h1 + h2
            mins = 10 * m1 + m2
            time = 60 * hours + mins
            if 0 <= hours < 24 and 0 <= mins < 60 and time > ans:
                ans = time

        return "{:02}:{:02}".format(*divmod(ans, 60)) if ans >= 0 else ""


