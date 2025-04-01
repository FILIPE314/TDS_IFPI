from turtle import *
shape("turtle")
speed(8)
color("red")
pensize(4)

triangulo = 360 / 3
quadrado = 360 / 4
pentagono = 360 / 5
hexagono = 360 / 6

for count in range(3):
    forward(100)
    right(triangulo)

left(90)
penup()
forward(100)
color("green")
pendown()

for count in range(4):
    forward(100)
    right(quadrado)

left(90)
penup()
forward(100)
color("red")
pendown()

for count in range(5):
    forward(100)
    right(pentagono)

left(90)
penup()
forward(100)
color("blue")
pendown()

for count in range(6):
    forward(100)
    right(hexagono)

done()