# função que calcula e retorna o valor do cálculo
def im_ou_p(numero):
    # variável local
    unidade = numero % 10
    # retorna o resutado caso seja esssa opção
    return unidade
# função que calcula e retorna o valor do cálculo
def im_ou_p2(numero):
    # variável local
    dezena = numero // 10
    # variável local
    dezena = dezena % 10
    # retorna o resutado caso seja esssa opção
    return dezena
# função que calcula e retorna o valor do cálculo
def im_ou_p3(numero):
    # variável local
    centena = numero // 10
    # variável local
    centena = centena // 10
    # retorna o resutado caso seja esssa opção
    return centena
# condicional(complementar) que verifica o resultado
def resultado(unidade,dezena,centena,numero):
    # condicional(complementar) que verifica o resultado
    if numero == 90:
        # imprime o resultado quando a função é acionada
        print('1')
    # condicional(complementar) que verifica o resultado
    elif numero == 100 or numero == 300 or numero == 500 or numero == 700 or numero == 900:
        # imprime o resultado quando a função é acionada
        print('2')
    # condicional(complementar) que verifica o resultado
    elif numero == 200 or numero == 400 or numero == 600 or numero == 800:
        # imprime o resultado quando a função é acionada
        print('3')
    # condicional(complementar) que verifica o resultado
    elif centena % 2 == 0 and dezena % 2 == 0 and unidade % 2 == 0:
        # imprime o resultado quando a função é acionada
        print('3')
    # condicional(complementar) que verifica o resultado
    elif centena % 2 > 0 and dezena % 2 == 0 and unidade % 2 == 0:
        # imprime o resultado quando a função é acionada
        print('2')
    # condicional(complementar) que verifica o resultado
    elif centena % 2 == 0 and dezena % 2 > 0 and unidade % 2 == 0:
        # imprime o resultado quando a função é acionada
        print('2')
    # condicional(complementar) que verifica o resultado
    elif centena % 2 == 0 and dezena % 2 == 0 and unidade % 2 > 0:
        # imprime o resultado quando a função é acionada
        print('2')
    # condicional(complementar) que verifica o resultado
    elif centena % 2 > 0 and dezena % 2 > 0 and unidade % 2 > 0:
        # imprime o resultado quando a função é acionada
        print('0')
    # condicional(falsa ou contrária)
    else:
        # imprime o resultado quando a função é acionada
        print('1')
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    numero = int(input().strip())
    # variável que guarda uma informação
    unidade = im_ou_p(numero)
    # variável que guarda uma informação
    dezena = im_ou_p2(numero)
    # variável que guarda uma informação
    centena = im_ou_p3(numero)
    # acionando a função
    resultado(unidade,dezena,centena,numero)
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()