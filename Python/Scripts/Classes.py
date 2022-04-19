'''class Person:
  def __init__(self, name, age, gender, weight, nbaTeam, nflTeam, collegeDegree, homeOwner, bornCity, currentCity):
    self.name = name
    self.age = age
    self.gender = gender
    self.weight = weight
    self.nbaTeam = nbaTeam
    self.nflTeam = nflTeam
    self.collegeDegree = collegeDegree
    self.homeOwner = homeOwner
    self.bornCity = bornCity
    self.currentCity = currentCity

  def myfunc(self):
    print("Hello my name is " + self.name + " I'm " + self.age)

  def detention(self): #loop my name and how many times i've been bad"
    for x in range(0,10):
      if self.gender == 1:
        answer = "boy"
      elif self.gender == 2:
        answer = "girl"
      else:
        answer = "gender"

      txt = "My name is {}, and I'm a bad {}"
      print(txt.format(self.name,answer))
      x+=1

  def details(self):
    print(self.weight + "lbs")

  def ConvoDetails(self):
    print("Collge Degree: " + self.collegeDegree)
    print("Fav Nba Team: " + self.nbaTeam)
    print("Fav NFL Team: " + self.nflTeam)
    if self.homeOwner == 'Y' or self.homeOwner == ' y':
      print("Home Owner: Yes")
    elif self.homeOwner == 'N' or self.homeOwner == 'n':
      print("Home Owner: No")
    else:
      print("Home Owner: Pending")

  def CityConverstation(self):
    if self.bornCity == 'Las Vegas':
      print("I'm from Vegas " + self.bornCity + " Born and Raised")
    else:
      print(self.bornCity)
    

    if self.currentCity == 'Dallas':
      print("I currently live in " + self.currentCity + " tho.")
    else:
      txt = "I'm finna move to {} tho"
      print(txt.format(self.currentCity))

p1 = Person("Rabb", str(27), 1, "190", "LA Lakers", "LA Chargers", "Computer Science","","Las Vegas","Dallas")
p1.myfunc()
p1.detention()
p1.details()
p1.ConvoDetails()
p1.CityConverstation()
'''


import csv
class Population():
  def __init__(self,rank,sentence,name,cc):
    self.rank = rank
    self.sentence = sentence
    self.name = name
    self.cc = cc
    
  def func():
    this_dict = {}
    with open ('/Users/khallidwilliams/Desktop/SampleCSVFile_11kb.csv', encoding="latin-1") as csv_file: 
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      ccTotal = 0
      for row in csv_reader:
        if row[1] == 'Newell 326':
          print('Skipping {}'.format(row))
          continue
        if row[1] == '600 Series Flip':
          print('{} is lit'.format(row[2]))
        if row[3] != '':
          ccTotal += int(row[3]) 
        line_count += 1
        this_dict.update({row[0] : [row[1],row[2],row[3]]})
      #print(this_dict)
      print('ccTotalv = {}'.format(ccTotal))
      return this_dict

csv_dict = Population.func()
obj_list = {}

for obj in csv_dict: #Loop thru dictionary
  obj_list.update(csv_dict) #update new dictionary after looping thru each line
  for i in obj_list: #loop thru new dictionary and grab values in the list
    for f in i: #loop thru each item in the list 
      key = obj_list.keys()
      Population(key,f,f,f) #name, [sentence, name, cc]

  print('{} : {}'.format(obj,obj_list.get(obj))) #print newly create object values
  print('Object {} created'.format(obj)) #print object is created