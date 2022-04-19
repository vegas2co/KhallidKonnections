num = 0
for i in range(1,10):
    #for j in range(i):
    num +=1
    if num < 2:
        print(str(i))
    else:
        print(str(i)+str(num))


for i in range(1,10):
    for j in range(i):
        print(i)