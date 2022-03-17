import unittest
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

def get_user_input():
  running = True
  while running:
    try:
      user_input = input('Enter your name: ')
      print('My name is Khallid')

      user_input_age = input('Enter Age: ')
      if int(user_input_age) == 28:
        print('WOW Me too')
      else:
        print('My age is 28')

      user_input_state = input('Enter your state: ')
      print('My state is Nevada')

      indexNumber = len(personDict)+1
      personDict['Girl number'] = indexNumber
      personDict['Name'] = user_input
      personDict['Age'] = user_input_age
      personDict['State'] = user_input_state
  
      bio = 'You are {} your from {} and your {} years old'.format(user_input,user_input_state,user_input_age)
      print(bio)
      print(personDict)
    except:
      print('Error: Could not enter Try/except.')

    done =  input('Done? ')
    if done == 'y':
      print('Ending...')
      break
    else:
      continue

  i = 0  
  while i < len(personDict):
    if i < 3:
      print('Daddy said -> Get yo weight up')
      break
    elif i >= 3 and i < 5:
      print('Daddy said -> Okay i see you yung buck')
      break
    else:
      print('Daddy said -> You just like ya daddy')
      break
'''
def solution(A):
  # write your code in Python 3.6
  list = []
  size = len(A)
  for i in range(0,size):
    for j in range(i+1,size):
      while True:
        answer = A[j] - A[i]
        list.append(answer)
        print(list)
        print('i = '+str(A[i]))
        print('j = '+str(A[j]))
        print(A)
        print('Pair with a given difference {} is {} & {} \n'.format(answer,A[j],A[i]))
        A.pop(0)
        '''
class Test(unittest.TestCase):
  def solution(A):
    list = []
    size = len(A)
    i = 0
    while i < size-1:
      if A[i] < A[i+1]:
        print('high')
        list.append('high')
        i+=1
      elif A[i] > A[i+1]:
        print('low')
        list.append('low')
        i+=1
      elif A[i] == A[i+1]:
        print("Equal")
        list.append('equal')
        i+=1
      else:
        print('EOL')
    print(list)


def average_scores_five(self, dictionary):
  try:
    thisdict = dictionary
    avg = 0
    for value in thisdict.values():
      print("{}".format(value))
      avg += value
    length = len(thisdict)
    avg = avg / length
    print('Average of 5 Scores = {}'.format(avg))
  except ZeroDivisionError:
    print(ZeroDivisionError)

  expected = 97.0
  actual = avg
  self.assertAlmostEqual(expected,actual)
  return 

def average_scores_zero(self, dictionary):
  try:
    thisdict = dictionary
    avg = 0
    for value in thisdict.values():
      if value == 97:
        break
      print("{}".format(value))
      avg += value
        
    length = len(thisdict)
    avg = avg / length
    print('Average of 0 Scores = {}'.format(avg))
  except ZeroDivisionError:
    print(ZeroDivisionError)

  expected = 0
  actual = avg
  self.assertAlmostEqual(expected,actual)
  return
  

if __name__ == "__main__":
  test_set = {1,1,2,3,2,4,3,4}
  test_value = 5
  #in_set(test_set,test_value)

  #avg_scores(get_test_scores())
  personDict = dict()
  #get_user_input()
  Alist = [2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 2, 5]
  p1 = Test.solution(Alist)
  unittest.main(p1)



