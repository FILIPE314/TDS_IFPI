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
    a = adicionar hobby
    d = remover hobby
    p = imprimir hobbies
    q = sair
''')

while executa == True:

    menuChoice = input('\n>_').lower()

    if menuChoice == 'c':        
        print(f'Aqui está o seu cumprimento, {nome}:')
        print(nome, 'você é', choice(adjetivos), 'em' ,choice(hobbies),'.')

    elif menuChoice == 'a':
        itemToAdd = input('Adicione o hobby: ')
        hobbies.append(itemToAdd)

    elif menuChoice == 'd':
        itemToDelete = input('Insira o hobby a ser removido: ')
        if itemToDelete in hobbies:
            hobbies.remove(itemToDelete)
        else:
            print('O hobby não está na lista.')

    elif menuChoice == 'p':
        print(hobbies)

    elif menuChoice == 'q':        
        executa = False

    else: 
        print('Escolha uma opção válida!!')