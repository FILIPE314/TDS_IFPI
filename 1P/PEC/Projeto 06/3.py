from turtle import *

# Um quadrado 
shape("square")
speed(8)

color("Red")
pensize(1)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)

# Triângulo

color("Blue")
right(90)
forward(50) 
left(120)  # 120 graus à esquerda
forward(50) 
left(120)
forward(50)

# Retangulo

color("Yellow")
right(60)
forward(100)
left(90)
forward(50)
left(90)
forward(100)
penup()
left(90)
forward(50)
left(90)
forward(100)
color("Orange")
pendown()
right(120)
forward(50)
right(60)
forward(100)
hideturtle()

done()