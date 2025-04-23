# função que define qual número é maior
def maior(num1,num2,num3,num4,num5):
    if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
        return num1
    elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
        return num2
    elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
        return num3
    elif num4 > num2 and num4 > num3 and num4 > num1 and num4 > num5:
        return num4
    elif num5 > num2 and num5 > num3 and num5 > num4 and num5 > num1:
        return num5
# função que define qual número é menor
def menor(num1,num2,num3,num4,num5):
    if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:
        return num1
    elif num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5:
        return num2
    elif num3 < num1 and num3 < num2 and num3 < num4 and num3 < num5:
        return num3
    elif num4 < num2 and num4 < num3 and num4 < num1 and num4 < num5:
        return num4
    elif num5 < num2 and num5 < num3 and num5 < num4 and num5 < num1:
        return num5
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    num1 = int(input().strip())
    # variável que imprime uma informação na tela e armazena dados
    num2 = int(input().strip())
    # variável que imprime uma informação na tela e armazena dados
    num3 = int(input().strip())
    # variável que imprime uma informação na tela e armazena dados
    num4 = int(input().strip())
    # variável que imprime uma informação na tela e armazena dados
    num5 = int(input().strip())
    # imprime uma informação na tela
    print(maior(num1,num2,num3,num4,num5))
    # imprime uma informação na tela
    print(menor(num1,num2,num3,num4,num5))
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()