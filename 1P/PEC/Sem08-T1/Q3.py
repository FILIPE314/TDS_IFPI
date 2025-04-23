# função que define qual número é maior
def maior(num1,num2,num3,num4,num5):
    if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
        return num1
    elif num1 < num2 and num1 > num3 and num1 > num4 and num1 > num5:
        return num2
    elif num1 > num2 and num1 < num3 and num1 > num4 and num1 > num5:
        return num3
    elif num1 > num2 and num1 > num3 and num1 < num4 and num1 > num5:
        return num4
    elif num1 > num2 and num1 > num3 and num1 > num4 and num1 < num5:
        return num5
# função que define qual número é menor
def menor(num1,num2,num3,num4,num5):
    if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:
        return num1
    elif num1 > num2 and num1 < num3 and num1 < num4 and num1 < num5:
        return num2
    elif num1 < num2 and num1 > num3 and num1 < num4 and num1 < num5:
        return num3
    elif num1 < num2 and num1 < num3 and num1 > num4 and num1 < num5:
        return num4
    elif num1 < num2 and num1 < num3 and num1 < num4 and num1 > num5:
        return num5
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
    # imprime uma informação na tela
    print('Essa é o maior número:',maior(num1,num2,num3,num4,num5))
    # imprime uma informação na tela
    print('Essa é o menor número:',menor(num1,num2,num3,num4,num5))
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()