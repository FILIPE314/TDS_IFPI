# função que compara e divide números
def comparacao(num1,num2,num3):
    if num2 == num1 or num3 == num1:
        return 0
    elif num2 < num1 and num3 < num1 and num2 > num3:
        return num1 - num2
    elif num3 < num1 and num2 < num1 and num3 > num2:
        return num1 - num3
    elif num2 < num1 and num1 - num2 < num3 - num1:
        return num1 - num2
    elif num3 < num1 and num1 - num3 < num2 - num1:
        return num1 - num3
    elif num2 - num1 == num1 - num3:
        return num2 - num1
    elif num2 - num1 > num3 - num1:
        return num3 - num1
    elif num2 - num1 < num3 - num1:
        return num2 - num1
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    num1 = int(input().strip())
    # variável que imprime uma informação na tela e armazena dados
    num2 = int(input().strip())
    # variável que imprime uma informação na tela e armazena dados
    num3 = int(input().strip())
    # acionando a função
    print(comparacao(num1,num2,num3))
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()