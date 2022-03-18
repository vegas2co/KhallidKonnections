
import unittest

class Scores(unittest.TestCase):
  def get_test_scores():
    scores_dict = dict()
    num_scores = input('Please enter number of test scores: ')
    i = 1
    while i < int(num_scores)+1:
      score = input('Please enter test score:')
      print(str(score))
      scores_dict["Test Score"+str(i)] = int(score)
      i+=1
    return scores_dict
  
  def test_avg_scores(self):
    test_scores = Scores.get_test_scores()
    print(test_scores)
    print('The number of scores in the dict is {}'.format(len(test_scores)))
    sum = 0
    for i in test_scores.values():
      sum = int(i) + sum
    avg = sum/len(test_scores)
    print('The average score is {}'.format(str(avg)))

if __name__ == "__main__":
  unittest.main()