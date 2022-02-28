'''
NOTES

2 colors left 30,45,60,90 for uniformaty
3 colors left 30,45,60,120 for uniformaty
4 colors left 30,45,90 for uniformaty
5 colors left 24 & 72 for uniformaty
6 colors left 20, 30, 60 for uniformaty
7 colors left 25.71, 51.29, 60 for uniformaty
8 colors left 22.5, 45, 60 for uniformaty

if left starts with a number it must remain that number
'''

import turtle
from time import sleep
colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'brown', 'pink']
test = turtle.Turtle()
test.color("orange")
test.pensize(5)
test.shape("arrow")

test.fillcolor(colors[2])
test.begin_fill()
test.forward(100)
sleep(1)
test.circle(45,180)
sleep(1)
test.right(180)
test.circle(45,180)
sleep(1)
test.forward(300)
sleep(1)
test.left(90)
test.forward(180)
test.left(90)
test.forward(300)
test.fillcolor(colors[2])
test.end_fill()
turtle.done()

'''
t.speed(0)
for x in range(1000):
    t.pencolor(colors[x%8]) 
    t.width(x//100)
    t.forward(x)
    t.left(60)
    if x >= 60:
        t.pencolor(colors[x%7])
        t.width(x//100)
        t.forward(x)
        t.left(60)
        print('At 60')

    if x >= 120:
        t.pencolor(colors[x%6])
        t.width(x//100)
        t.forward(x)
        t.left(60)
        print('At 120')
    if x >= 180:
        t.pencolor(colors[x%3])
        t.width(x//100)
        t.forward(x)
        t.left(60)
        print('At 180')

    if x >= 240:
        t.pencolor(colors[x%6])
        t.width(x//100)
        t.back(x)
        t.left(89)
        print('At 240')
    if x >= 300 and x <= 360:
        t.pencolor(colors[x%6])
        t.width(x//100)
        t.back(x)
        t.left(99)
        print('At 300')
    '''