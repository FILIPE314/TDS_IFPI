# função que calcula dois valores conforme oque o usuário escolher
def calc(num1,num2,operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        return num1 / num2
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    num1 = int(input().strip())
    # variável que imprime uma informação na tela e armazena dados
    num2 = int(input().strip())
    # variável que imprime uma informação na tela e armazena dados
    operacao = int(input().strip())
    # acionando a função
    print(calc(num1,num2,operacao))
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()