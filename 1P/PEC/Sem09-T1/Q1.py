# função que calcula(entre três dígitos) quais os valores são iguais
def comparacao(num1, num2, num3):
    if num1 == num2 and num2 == num3:
        return 'Todos os valores são iguais'
    elif num1 != num2 and num2 != num3:
        return 'Todos os valores são diferentes'
    else:
        return 'Existem dois valores iguais e um diferente'
# função (main) que inicia e termina o programa
def main():
    # imprime uma informação na tela
    print('Digite 3 números inteiros para saber quantos valores são iguais:')
    # variável que imprime uma informação na tela e armazena dados
    num1 = int(input('Digite um valor qualquer'))
    # variável que imprime uma informação na tela e armazena dados
    num2 = int(input('Digite um valor qualquer'))
    # variável que imprime uma informação na tela e armazena dados
    num3 = int(input('Digite um valor qualquer'))
    # acionando a função
    print(comparacao(num1,num2,num3))
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()