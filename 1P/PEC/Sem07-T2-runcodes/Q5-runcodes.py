# condicional que faz cálculos para obter o resultado
def crescente(num1,num2,num3,maximo,minimo):
    # variável local
    soma = num1 + num2 + num3
    # variável local
    soma2 = maximo + minimo
    # variável local
    soma3 = soma - soma2
    # imprime uma mensagem na tela quando a função é acionada
    return soma3
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    num1 = int(input().strip())
    # variável que imprime uma informação na tela e armazena dados
    num2 = int(input().strip())
    # variável que imprime uma informação na tela e armazena dados
    num3 = int(input().strip())
    # variável que calcula o máximo número entre as opções e armazena dados
    maximo = max(num1,num2,num3)
    # variável que calcula o mínimo número entre as opções e armazena dados
    minimo = min(num1,num2,num3)
    # imprime o resultado na tela 
    print(minimo)
    # imprime o resultado na tela
    print(crescente(num1,num2,num3,maximo,minimo))
    # imprime o resultado na tela
    print(maximo)
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()