def Birthday(bday):
  return bday[0:2]+'/'+bday[2:4]+'/'+bday[4:]

def myName(name):
  return "My name is " + name

#The city function that chooses a city 
def city():
  theList = ["Atlanta", "Houston", "Chicago", "Detroit", "Baltimore", "Los Angeles", "Las Vegas", "Memphis", "Denver", "Miami"]
  sheFrom = input("Where you from? ")
  print("She said: I'm from " + sheFrom)
  print("Me: Bet im from " + theList[4])

# Funuction to return a name
def name():
  user = input("Me: Hi what is your name?")
  print("Her name is " + user)
  print(' you have a pretty name')

def birthday():
  month = '03'
  day = '05'
  year = '1994'
  print("When is your birthday?")
  answer = input("Enter first: ")
  print(answer)

  if (
      (answer[4:] < year) or #year
      ((answer[4:] == year) and (answer[2:4] < day)) or #year & month
      ((answer[4:] == year) and (answer[2:4] < day) and (answer[0:2] < month)) #year, month, day
    ):
    print("She got you beat bros")
  else:
    print("You Won the war bros.")

def age(femaleAge):
  rabb = 25
  if rabb > femaleAge:
    ageLimit = 21
    print("Bro you older than her")
    if femaleAge < ageLimit:
      print("But bro she under the limit. You willing to take that chance?")
      print("Maybe lol")
    else:
      print("And she age appropriate she gucci!")
  elif rabb == femaleAge:
    print("Bro yall the same age. Now you gotta see who older tho")
    name()
    birthday()
    if '03/05/1994' < Birthday('03051994'):
        print("Damn bris she got you")
    else:
        print("You the OG over here")
    city()
  else:
    print("You to young for me sorry.")

age(25)

def talk():
  what_up = "Whats up G"
  wyo = "What you on foo"
  no_shit = "Not Shit"
  a = what_up
  while(a):
    print(a)
    if (a):
        print(wyo)
    break
  print(no_shit)
