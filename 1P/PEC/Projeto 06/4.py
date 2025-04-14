from turtle import *

speed(10)
shape("turtle")

# Pentágono
for count in range(5):
    forward(50)
    right(72)

# Hexágono

penup()
forward(100)
pendown()
for count in range(6):
    forward(50)
    right(60)

# Circulo 

penup()
left(90)
forward(100)
pendown()   

for count in range(360):
    forward(1)  
    right(1) 

hideturtle()

done()