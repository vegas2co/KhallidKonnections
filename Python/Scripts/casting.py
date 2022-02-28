def casting(input):
    print(float(input))

def blah(input):
    print(input + '\n')
    casting(490)
    
#blah("hi mom")

def young():
    print('Young ass nigga')

def grown():
    print('Grown ass nigga')

def age(input):
    age = input
    if age < 18:
        young()
    else:
        grown()

price = input("Price: ")
cash_off = input("cash off: ")
precentage = input("percentage: ")
tax = 1.06

def cashout():
    CASH_OFF_TOTAL = ((int(price) - int(cash_off)) * float(pre))
    print(CASH_OFF_TOTAL)

    if CASH_OFF_TOTAL >= 50:
        shipping = 0
        print('shipping = ' + str(shipping))
        CASH_OFF_TOTAL = (CASH_OFF_TOTAL + shipping) * tax
        CASH_OFF_TOTAL = '{:.2f}'.format(CASH_OFF_TOTAL)
        print('Total = ' + str(CASH_OFF_TOTAL))

    elif CASH_OFF_TOTAL >= 30 and CASH_OFF_TOTAL < 50:
        shipping  = 11.95
        print('shipping = ' + str(shipping))
        CASH_OFF_TOTAL = (CASH_OFF_TOTAL + shipping) * tax
        CASH_OFF_TOTAL = '{:.2f}'.format(CASH_OFF_TOTAL)
        print('Total = ' + str(CASH_OFF_TOTAL))

    elif CASH_OFF_TOTAL >= 10 and CASH_OFF_TOTAL < 30:
        shipping  = 7.95
        print('shipping = ' + str(shipping))
        CASH_OFF_TOTAL = (CASH_OFF_TOTAL + shipping) * tax
        CASH_OFF_TOTAL = '{:.2f}'.format(CASH_OFF_TOTAL)
        print('Total = ' + str(CASH_OFF_TOTAL))

    else:
        shipping  = 5.95
        print('shipping = ' + str(shipping))
        CASH_OFF_TOTAL = (CASH_OFF_TOTAL + shipping) * tax
        CASH_OFF_TOTAL = '{:.2f}'.format(CASH_OFF_TOTAL)
        print('Total = ' + str(CASH_OFF_TOTAL))

if precentage == '10':
    pre = .9

    cashout()

elif precentage == '15':
    pre = .85

    cashout()

elif precentage == '20':
    pre = .8

    cashout()
else:
    print('Error')
