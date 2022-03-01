def casting(input):
  print(float(input))

def blah(input):
  print(input + '\n')
  casting(490)
    
#blah("hi mom")

def young():
  print('Young man')

def grown():
  print('Grown man')

def age(input):
  age = input
  if age < 18:
    young()
  else:
    grown()

price = input("Price: ") #Get Price
cash_off = input("cash off: ") #Get cash off coupon 5 or 10
percentage = input("percentage: ") #Get percentage off
tax = 1.06

def cashout():
  CASH_OFF_TOTAL = (float(price) - float(cash_off)) * float(pre) #Total calculation
  print(CASH_OFF_TOTAL)  #Display total before shippiong and tax.

  if CASH_OFF_TOTAL >= 50:
    shipping = 0
    print('shipping = ' + str(shipping)) #Display shipping added to total
    CASH_OFF_TOTAL = (CASH_OFF_TOTAL + shipping) * tax #Calculate total + shipping and tax
    CASH_OFF_TOTAL = '{:.2f}'.format(CASH_OFF_TOTAL) #Turn updated total to 2 decimal points
    print('Total = ' + str(CASH_OFF_TOTAL)) #Official total

  elif CASH_OFF_TOTAL >= 30 and CASH_OFF_TOTAL < 50:
    shipping = 11.95
    print('shipping = ' + str(shipping))
    CASH_OFF_TOTAL = (CASH_OFF_TOTAL + shipping) * tax
    CASH_OFF_TOTAL = '{:.2f}'.format(CASH_OFF_TOTAL)
    print('Total = ' + str(CASH_OFF_TOTAL))

  elif CASH_OFF_TOTAL >= 10 and CASH_OFF_TOTAL < 30:
    shipping = 7.95
    print('shipping = ' + str(shipping))
    CASH_OFF_TOTAL = (CASH_OFF_TOTAL + shipping) * tax
    CASH_OFF_TOTAL = '{:.2f}'.format(CASH_OFF_TOTAL)
    print('Total = ' + str(CASH_OFF_TOTAL))

  else:
    shipping = 5.95
    print('shipping = ' + str(shipping))
    CASH_OFF_TOTAL = (CASH_OFF_TOTAL + shipping) * tax
    CASH_OFF_TOTAL = '{:.2f}'.format(CASH_OFF_TOTAL)
    print('Total = ' + str(CASH_OFF_TOTAL))

if percentage == '10':
  pre = .9
  cashout()

elif percentage == '15':
  pre = .85
  cashout()

elif percentage == '20':
  pre = .8
  cashout()
else:
  print('Error')
