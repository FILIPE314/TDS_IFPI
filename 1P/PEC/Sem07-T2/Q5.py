# condicional que faz cálculos para obter o resultado
def crescente(num1,num2,num3):
    # variável local
    soma = num1 + num2 + num3
    # variável local
    maximo = max(num1,num2,num3)
    # variável local
    minimo = min(num1,num2,num3)
    # variável local
    soma2 = maximo + minimo
    # imprime uma mensagem na tela quando a função é acionada
    print(minimo,(soma - soma2),maximo)
# função (main) que inicia e termina o programa
def main():
    # imprime uma mensagem na tela
    print('Digite três números em qualquer ordem para ficarem em ordem crescente.')
    # variável que imprime uma informação na tela e armazena dados
    num1 = int(input('Digite o primeiro número:').strip())
    # variável que imprime uma informação na tela e armazena dados
    num2 = int(input('Aqui o segundo:').strip())
    # variável que imprime uma informação na tela e armazena dados
    num3 = int(input('E aqui o terceiro:').strip())
    # acionando a função
    crescente(num1,num2,num3)
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()