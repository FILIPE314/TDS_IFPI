from turtle import *
shape("turtle")
speed(5)
color("darkblue")
pensize(4)

for count in range(5):
    forward(100)
    right(72)

left(90)
penup()
forward(50)
right(90)
color("grey")
pendown()

for count in range(6):
    forward(100)
    left(60)

right(180)
penup()
forward(200)
color("lightgreen")
pendown()

for count in range(120):
    forward(3)
    left(3)

right(90)
penup()
color("black")
forward(150)
right(130)

done()