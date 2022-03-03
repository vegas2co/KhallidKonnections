import string
def hourly_employee_input():
    username = input('What is your name:')
    if username not in string.punctuation:
        print(username)
    else:
        username = ('milk')
        print(username)

    hours = int(input('How many hours did you have:'))
    if hours > 0:
        print(hours)
    elif hours < 0:
        hours = 0
        print(hours)
    hourlyrate = float(input('What is your houry rate:'))

    return username, str(hours), str(hourlyrate)



def weekly_pay(username, hours, hourlyrate):
    dollars = float(hours) * float(hourlyrate)
    print('Your name is {} you worked {}hrs and your rate of pay is {} \n  && his weekly pay is {}'.format(username,str(hours),str(hourlyrate), dollars))

a, b, c = hourly_employee_input()

weekly_pay(a,str(b),str(c))
