from turtle import *

lados = int(input("Digite a quantidade de lados da figura: "))
angulo = 360 / lados

for count in range(lados):
    forward(100)
    right(angulo)

done()