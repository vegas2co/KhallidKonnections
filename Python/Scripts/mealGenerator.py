import random as r

proteinList = ['Chicken', 'Ground Turkey', 'Shrimp', 'Salmon']
veggiesList = ['Brocolli', 'Zucchini', 'Spinach', 'Kale']
carbsList = ['Sweet Potatoes', 'Noodles', 'Jasmine Rice', 'Toast']
drink = ['Protein Drink']

breakfastList = ['Eggs & toast', 'Oatmeal']

def dailyMeals():
    breakfast = r.choice(breakfastList)
    meats = r.choice(proteinList)
    veggies = r.choice(veggiesList)
    carbs = r.choice(carbsList)

    breakfastSentence = 'For breakfast I will be eatiing {}'.format(breakfast)
    lunchSentence = 'For lunch I will be eatiing a healthy serving of {}, {}, {} with a {}'.format(meats,veggies,carbs,drink[0])
    dinnerSentence = 'For dinner I will be eatiing a healthy serving of {} {} {}'.format(meats,veggies,carbs)

    print(breakfastSentence)
    print(lunchSentence)
    print(dinnerSentence + '\n')
    
    p = meats

    proteinList.remove(p)
    print(breakfastSentence)
    print(lunchSentence)
    print(dinnerSentence + '\n')


dailyMeals()