from datetime import date

user_name = input('enter your name: ')
user_age = input('enter your age: ')
today = date.today()

print('Hello ' + user_name + '! You are ' + user_age + ' years old.')
print('That means you were born in the ' + str(today.year - int(user_age)))