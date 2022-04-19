'''
By: Khallid Williams
Program to get the average score by entering
How many scores, and entering each score individually!
'''
import unittest
class Scores(unittest.TestCase):
  def get_test_scores():
    scores_dict = dict()
    try:
      num_scores = input('Please enter number of test scores: ')
      i = 1
      while i < int(num_scores)+1:
        score = input('Please enter test score:')
        print(str(score))
        scores_dict["Test Score"+str(i)] = int(score)
        i+=1
    except ValueError:
      print(ValueError)
    return scores_dict
  
  def get_avg_scores(self):
    test_scores = Scores.get_test_scores()
    print(test_scores)
    print('The number of scores in the dict is {}'.format(len(test_scores)))
    sum = 0
    for i in test_scores.values():
      sum = int(i) + sum
    avg = sum/len(test_scores)
    return avg

  def test_grades(self):
    overall_score = Scores.get_avg_scores(self)
    print('The average score is {}'.format(str(overall_score)))
    if overall_score >= 90:
      print('You received an A for the class')
    elif overall_score >= 80:
      print('You received a B for the class')
    elif overall_score >= 70:
      print('You received an C for the class')
    elif overall_score >= 60:
      print('You received an D for the class')
    else:
      print('You Failed the class')

'''class Cars(unittest.TestCase):
  def __init__(self,make,model,year):
    self.make = make
    self.model = model
    self.year = year
  
  def test_myCar(self):
    #y = input('Year')
    #M = input('Make')
    #m = input('Model')
    return 'My car is a {} {} {}'.format(self.year,self.make,self.model)'''

if __name__ == "__main__":
  unittest.main() #Testing scores
  #car1 = Cars('2018', 'Toytota', 'Camry')
  #print(car1.myCar())
  #car2 = Cars('2007', 'Nissan', 'Maxima')
  #print(car2.myCar())