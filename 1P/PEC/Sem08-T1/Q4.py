# função para calcular a média
def med(num1,num2,num3,num4,num5):
    return (num1 + num2 + num3 + num4 + num5) / 5
# função que define qual número é maior
def maior(num1,media):
    if num1 > media:
        print(f'{num1:.2f}')
# função que define qual número é maior
def maior2(num2,media):
    if num2 > media:
        print(f'{num2:.2f}')
# função que define qual número é maior
def maior3(num3,media):
    if num3 > media:
        print(f'{num3:.2f}')
# função que define qual número é maior
def maior4(num4,media):
    if num4 > media:
        print(f'{num4:.2f}')
# função que define qual número é maior
def maior5(num5,media):
    if num5 > media:
        print(f'{num5:.2f}')
# função (main) que inicia e termina o programa
def main():
    # imprime uma informação na tela
    print('Digite duas datas para ser calculado qual das duas é a mais recente')
    # variável que imprime uma informação na tela e armazena dados
    num1 = int(input('Digite aqui um número:'))
    # variável que imprime uma informação na tela e armazena dados
    num2 = int(input('Digite aqui um número:'))
    # variável que imprime uma informação na tela e armazena dados
    num3 = int(input('Digite aqui um número:'))
    # variável que imprime uma informação na tela e armazena dados
    num4 = int(input('Digite aqui um número:'))
    # variável que imprime uma informação na tela e armazena dados
    num5 = int(input('Digite aqui um número:'))
    # variável que armazena dados
    media = med(num1,num2,num3,num4,num5)
    # imprime uma informação na tela
    print(f'Essa é a média entre os 5 números {med(num1,num2,num3,num4,num5):.2f} e abaixo os números maiores que a média')
    # aciona a função
    maior(num1,media)
    # aciona a função
    maior2(num2,media)
    # aciona a função
    maior3(num3,media)
    # aciona a função
    maior4(num4,media)
    # aciona a função
    maior5(num5,media)
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()