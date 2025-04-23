from random import *

executa = True

adjetivos = ['maravilhoso','incrivel', 'excelente']
hobbies = ['andar de bicicleta', 'programar', 'fazer cha']

print('Gerador de Cumprimentos')
print('-----------------------')

nome = input('Qual seu nome? ')
print('''
Menu
    c = obter cumprimento
    q = sair
''')

while executa == True:

    menuChoice = input('\n>_').lower()

    if menuChoice == 'c':

        print(f'Aqui está o seu cumprimento, {nome}:')
        print(nome, 'você é', choice(adjetivos), 'em' ,choice(hobbies),'.')

    elif menuChoice == 'q':

        executa = False

    else: 
        print('Escolha uma opção válida!!')