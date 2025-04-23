# condicional(complementar) que verifica o resultado
def sig(dia,mes):
    # condicional(complementar) que verifica a resposta do usuário
    if 21 <= dia <= 31 and mes == 3:
        # imprime o resultado quando a função é acionada
        print('Áries')
    # condicional(complementar) que verifica a resposta do usuário
    elif 1 <= dia <= 19 and mes == 4:
        # imprime o resultado quando a função é acionada
        print('Áries')
    # condicional(complementar) que verifica a resposta do usuário
    elif 20 <= dia <= 30 and mes == 4:
        # imprime o resultado quando a função é acionada
        print('Touro')
    # condicional(complementar) que verifica a resposta do usuário
    elif 1 <= dia <= 20 and mes == 5:
        # imprime o resultado quando a função é acionada
        print('Touro')
    # condicional(complementar) que verifica a resposta do usuário
    elif 21 <= dia <= 31 and mes == 5:
        # imprime o resultado quando a função é acionada
        print('Gêmeos')
    # condicional(complementar) que verifica a resposta do usuário
    elif 1 <= dia <= 21 and mes == 6:
        # imprime o resultado quando a função é acionada
        print('Gêmeos')
    # condicional(complementar) que verifica a resposta do usuário
    elif 22 <= dia <= 30 and mes == 6:
        # imprime o resultado quando a função é acionada
        print('Câncer')
    # condicional(complementar) que verifica a resposta do usuário
    elif 1 <= dia <= 22 and mes == 7:
        # imprime o resultado quando a função é acionada
        print('Câncer')
    # condicional(complementar) que verifica a resposta do usuário
    elif 23 <= dia <= 31 and mes == 7:
        # imprime o resultado quando a função é acionada
        print('Leão')
    # condicional(complementar) que verifica a resposta do usuário
    elif 1 <= dia <= 22 and mes == 8:
        # imprime o resultado quando a função é acionada
        print('Leão')
    # condicional(complementar) que verifica a resposta do usuário
    elif 23 <= dia <= 31 and mes == 8:
        # imprime o resultado quando a função é acionada
        print('Virgem')
    # condicional(complementar) que verifica a resposta do usuário
    elif 1 <= dia <= 22 and mes == 9:
        # imprime o resultado quando a função é acionada
        print('Virgem')
    # condicional(complementar) que verifica a resposta do usuário
    elif 23 <= dia <= 30 and mes == 9:
        # imprime o resultado quando a função é acionada
        print('Libra')
    # condicional(complementar) que verifica a resposta do usuário
    elif 1 <= dia <= 22 and mes == 10:
        # imprime o resultado quando a função é acionada
        print('Libra')
    # condicional(complementar) que verifica a resposta do usuário
    elif 23 <= dia <= 31 and mes == 10:
        # imprime o resultado quando a função é acionada
        print('Escorpião')
    # condicional(complementar) que verifica a resposta do usuário
    elif 1 <= dia <= 21 and mes == 11:
        # imprime o resultado quando a função é acionada
        print('Escorpião')
    # condicional(complementar) que verifica a resposta do usuário
    elif 22 <= dia <= 30 and mes == 11:
        # imprime o resultado quando a função é acionada
        print('Sagitário')
    # condicional(complementar) que verifica a resposta do usuário
    elif 1 <= dia <= 21 and mes == 12:
        # imprime o resultado quando a função é acionada
        print('Sagitário')
    # condicional(complementar) que verifica a resposta do usuário
    elif 22 <= dia <= 31 and mes == 12:
        # imprime o resultado quando a função é acionada
        print('Capricórnio')
    # condicional(complementar) que verifica a resposta do usuário
    elif 1 <= dia <= 19 and mes == 1:
        # imprime o resultado quando a função é acionada
        print('Capricórnio')
    # condicional(complementar) que verifica a resposta do usuário
    elif 20 <= dia <= 31 and mes == 1:
        # imprime o resultado quando a função é acionada
        print('Aquário')
    # condicional(complementar) que verifica a resposta do usuário
    elif 1 <= dia <= 18 and mes == 2:
        # imprime o resultado quando a função é acionada
        print('Aquário')
    # condicional(complementar) que verifica a resposta do usuário
    elif 19 <= dia <= 28 and mes == 2:
        # imprime o resultado quando a função é acionada
        print('Peixes')
    # condicional(complementar) que verifica a resposta do usuário
    elif 1 <= dia <= 20 and mes == 3:
        # imprime o resultado quando a função é acionada
        print('Peixes')
    # condicional(falsa ou contrária)
    else:
        # imprime o resultado quando a função é acionada
        print('Esse dia e mês não existe')
# função (main) que inicia e termina o programa
def main():
    # imprime uma mensagem na tela
    print('Digite o dia em que nasceu e o mês para saber qual é o seu signo.')
    # variável que imprime uma informação na tela e armazena dados
    dia = int(input('Digite o dia em que você nasceu:').strip())
    # variável que imprime uma informação na tela e armazena dados
    mes = int(input('E aqui o mês em que nasceu:').strip())
    # acionando a função
    sig(dia,mes)
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()