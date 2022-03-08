
'''
import string
def hourly_employee_input():
	username = input('What is your name? ')
	if username not in string.punctuation:
		print(username)
	else:
		username = ('milk')
		print(username)

	hours = int(input('How many hours did you work? '))
	if hours > 0:
		print(hours)
	elif hours < 0:
		hours = 0
		print(hours)

	hourlyrate = float(input('What is your houry rate? '))
	if hourlyrate > 0:
		print(hourlyrate)
	elif hourlyrate < 0:
		hourlyrate = 0
		print(hourlyrate)

	return username, str(hours), str(hourlyrate)



def weekly_pay(username, hours, hourlyrate):
	dollars = float(hours) * float(hourlyrate)
	print('{} you worked {} hours this week.\nYour rate of pay is {} per hour.\nYour weekly pay is {}'.format(username,str(hours),str(hourlyrate), dollars))

a,b,c = hourly_employee_input()

weekly_pay(a,str(b),str(c))
'''

def numberRange():
  food = []
  user_input = int(input('Enter a number between 1 and 100: '))

  while user_input not in range(1,100):
    food.append(user_input)
    print(food)
    user_input = int(input('Another Attempt -> Enter a number between 1 and 100 : '))
  else:
    food.append(user_input)
    print(food)

numberRange()
	