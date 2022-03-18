
import unittest
import string

'''
Employee hourly pay calculator logic
weekly_pay() run the full thing
'''
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


'''
#Mar 15th 2022 7:00PM
Check if a number is in a set
'''
def in_set(incoming_set,user_number):
  if user_number in incoming_set:
    boolValue = user_number in incoming_set
    print('The boolean value is {}'.format(boolValue))
    print('The value {} is in the set {}'.format(user_number,incoming_set))
  else:
    boolValue = user_number in incoming_set
    print('The boolean value is {}'.format(boolValue))
    print('The value {} is not in the set {}'.format(user_number,incoming_set))


'''
AI Practice, Ask questions and reply automaticlly
end when pressing Y whena asked.
'''

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
  Mar 16th 3:00pm
  Test program when i had an interview at smoothstack!
'''     
class Interview(unittest.TestCase):
  def test_solution(A):
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


'''
  Mar 17th 6:00pm
  Helping -> Tutoring homework problem.
  Working with average scores of 5 and 0.
'''

#By Khallid Williams
#Unittest Scores class that has 3 functions
#1. test average scores by parametesrs #test1 = Scores().test_average_score(4,3,2,1,first_name = 'Khallid', last_name='Williams\n')
#2. test_average_scores_five with hard code dictionary
#3. test_average_scores_zero with empty dictionary -> should return error

class Scores(unittest.TestCase):
  def test_average_score(self,*args, **kwargs):
    print('Testing test_average_score')
    for i in args:
      print(i)
    for key, value in kwargs.items():
      print("%s == %s" % (key, value))
    return

  def test_average_scores_five(self):
    print('Testing test_average_scores_five')
    try:
      thisdict = {"test1": 99,"test2": 98,"test3": 97,"test4": 96,"test5": 95}
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
    self.assertTrue(expected,actual)
    return 

  def test_average_scores_zero(self):
    print('Testing test_average_scores_zero')
    try:
      thisdict = {}
      avg = 0
      for value in thisdict.values():
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

class Conditional(unittest.TestCase):
  def test_switch_case(i):
    print('Testing switch case statement')
    switcher={
      'Novice':50,
      'Beginner':150,
      'Expert':350,
      'Advanced':500
    }
    print('{} starts with {} points'.format(i,switcher.get(i,"Invalid Player Level")))
    #print(i in switcher)


if __name__ == "__main__":
  #a,b,c = hourly_employee_input()
  #weekly_pay(a,str(b),str(c))

  #test_set = {1,1,2,3,2,4,3,4}
  #test_value = 5
  #in_set(test_set,test_value)

  personDict = dict()
  #get_user_input()

  Alist = [2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 2, 5]
  Interview().test_solution(Alist)

  unittest.main()
