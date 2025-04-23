from random import *

executa = True

animais_machos = ['Acerola','Hulk','Bic','Scooby','Bolt','Sid','Malfoy','Bartolomeu','Simba']
animais_femeas = ['Luna','Bonnie','Mel','Jujuba','Maggie','Carrie','Pandora','Nala','Belina']

print('Serviço de nscolha de nome para animais de estimação')
print('----------------------------------------------------')

nome = input('Qual seu nome? ')
print('''
Menu
    c = obter nome
    a = adicionar nome
    d = remover nome
    q = sair
''')

while executa == True:

    menuChoice = input('\n>_').lower()

## Obter nome    
    if menuChoice == 'c':             
        genero = input('''
É macho ou fêmea?

Menu
    m = macho
    f = fêmea
    
>_
''')  
        print(f'Aqui está a sugestão, {nome}:')
        if genero.lower() == 'm':
            print(nome, 'você deve chamar seu animal de estimação de', choice(animais_machos),'.')
        elif genero.lower() == 'f':
            print(nome, 'você deve chamar seu animal de estimação de', choice(animais_femeas),'.')
        else:
            print('Escolha uma opção válida!!')


## Adicionar nome                
    elif menuChoice == 'a':
        itemToAdd = input('Adicione um nome: ')
        genero = input('''
É macho ou fêmea?

Menu
    m = macho
    f = fêmea
    
>_
''')  
        if genero.lower() == 'm':
            if itemToAdd not in animais_machos:
                animais_machos.append(itemToAdd)
            else:
                print('O nome já está na lista.')

        elif genero.lower() == 'f':
            if itemToAdd not in animais_femeas:
                animais_femeas.append(itemToAdd)
            else:
                print('O nome já está na lista.')

        else:
            print('Escolha uma opção válida!!')

## Remover nome                         
    elif menuChoice == 'd':
        itemToDelete = input('Insira o hobby a ser removido: ')
        genero = input('''
É macho ou fêmea?

Menu
    m = macho
    f = fêmea
    
>_
''')  
        if genero.lower() == 'm':
            if itemToDelete in animais_machos:
                animais_machos.remove(itemToDelete)
            else:
                print('O nome não está na lista.')

        elif genero.lower() == 'f':
            if itemToDelete in animais_femeas:
                animais_femeas.remove(itemToDelete)
            else:
                print('O nome não está na lista.')

        else:
            print('Escolha uma opção válida!!')

## interrompe o laço               
    elif menuChoice == 'q':        
        executa = False

    else: 
        print('Escolha uma opção válida!!')