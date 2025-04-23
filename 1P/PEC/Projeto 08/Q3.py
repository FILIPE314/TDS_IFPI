from random import *

print('Gerador de Cumprimentos')
print('-----------------------')

nome = input('Qual seu nome? ')
adjetivos = ['excelente','maravilhoso','incrivel','acima da média', 'excepcional', 'fenomenal' ]
hobbies = ['andar de bicicleta', 'programar', 'fazer pizza', 'jogar bola', 'correr']

print(nome, 'você é', choice(adjetivos), 'em' ,choice(hobbies),'.')