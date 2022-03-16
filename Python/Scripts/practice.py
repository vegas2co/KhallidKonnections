
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

#Mar 15th 2022 7:00PM

def in_set(incoming_set,user_number):
  if user_number in incoming_set:
    boolValue = user_number in incoming_set
    print('The boolean value is {}'.format(boolValue))
    print('The value {} is in the set {}'.format(user_number,incoming_set))
  else:
    boolValue = user_number in incoming_set
    print('The boolean value is {}'.format(boolValue))
    print('The value {} is not in the set {}'.format(user_number,incoming_set))

def get_test_scores():
  scores_dict = dict()
  num_scores = input('Please enter number of test scores: ')
  
  i = 1
  while i < int(num_scores):
    score = input('Please enter test score:')
    print(str(score))
    scores_dict["Test Score"+str(i)] = int(score)
    i+=1

  return scores_dict

def avg_scores(test_scores):
  print(test_scores)
  print('The number of scores equal {}'.format(len(test_scores)))
  sum = 0
  for i in test_scores.values():
    sum = int(i) + sum
  avg = sum/len(test_scores)
  print('The average score is {}'.format(str(avg)))


if __name__ == "__main__":
  test_set = {1,1,2,3,2,4,3,4}
  test_value = 5
  in_set(test_set,test_value)

  avg_scores(get_test_scores())




