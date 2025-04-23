# função que calcula e retorna o valor do cálculo
def inverter(numero):
    x = numero % 10
    numero = numero // 10
    y = numero % 10
    numero = numero // 10
    z = numero % 10
    numero = numero // 10
    w = numero % 10
    result = (x * 1000) + (y * 100) + (z * 10) + w
    return result
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazenam dados
    numero = int(input('Coloque um número de 1000 a 9999 para ele ser gerado ao contrário:'))
    # imprimindo o resultado na tela do computador do usuário
    print(inverter(numero))
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()