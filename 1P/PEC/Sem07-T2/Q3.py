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
# condicional(complementar) que verifica o resultado
def resultado(unidade,dezena,numero):
    # condicional(complementar) que verifica o resultado
    if numero < 10 or numero > 99:
        # imprime o resultado quando a função é acionada
        print('Tem que ser entre 10 a 99')
    # condicional(complementar) que verifica o resultado
    elif numero == 10 or numero == 30 or numero == 50 or numero == 70 or numero == 90:
        # imprime o resultado quando a função é acionada
        print('Apenas um dígito é ímpar.')
    # condicional(complementar) que verifica o resultado
    elif numero == 20 or numero == 40 or numero == 60 or numero == 80:
        # imprime o resultado quando a função é acionada
        print('Nenhum dígito é ímpar.')
    # condicional(complementar) que verifica o resultado
    elif dezena % 2 == 0 and unidade % 2 == 0:
        # imprime o resultado quando a função é acionada
        print('Nenhum dígito é ímpar.')
    # condicional(complementar) que verifica o resultado
    elif dezena % 2 > 0 and unidade % 2 == 0:
        # imprime o resultado quando a função é acionada
        print('Apenas um dígito é ímpar.')
    # condicional(complementar) que verifica o resultado
    elif dezena % 2 == 0 and unidade % 2 > 0:
        # imprime o resultado quando a função é acionada
        print('Apenas um dígito é ímpar.')
    # condicional(complementar) que verifica o resultado
    elif dezena % 2 > 0 and unidade % 2 > 0:
        # imprime o resultado quando a função é acionada
        print('Os dois dígitos são ímpares.')
    # condicional(falsa ou contrária)
    else:
        # imprime o resultado quando a função é acionada
        print('Apenas um dígito é ímpar.')
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    numero = int(input('Digite um número de 10 a 99 para saber quantos dígitos pare e ímpares ele tem:').strip())
    # variável que guarda uma informação
    unidade = im_ou_p(numero)
    # variável que guarda uma informação
    dezena = im_ou_p2(numero)
    # acionando a função
    resultado(unidade,dezena,numero)
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()