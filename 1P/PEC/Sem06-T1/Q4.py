# função que calcula qual o maior número
def maior(numero1,numero2,numero3,numero4,numero5):
    # retorna o valor calculado
    return max(numero1,numero2,numero3,numero4,numero5)
# função que calcula qual o menor número
def menor(numero1,numero2,numero3,numero4,numero5):
    # retorna o valor calculado
    return min(numero1,numero2,numero3,numero4,numero5)
# função que calcula qual a média entre todos os números
def media(numero1,numero2,numero3,numero4,numero5):
    # retorna o valor calculado
    return (numero1 + numero2 + numero3 + numero4 + numero5) / 5
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazenam dados
    numero1 = int(input('Digite um número:'))
    # variável que imprime uma informação na tela e armazenam dados
    numero2 = int(input('Digite um número:'))
    # variável que imprime uma informação na tela e armazenam dados
    numero3 = int(input('Digite um número:'))
    # variável que imprime uma informação na tela e armazenam dados
    numero4 = int(input('Digite um número:'))
    # variável que imprime uma informação na tela e armazenam dados
    numero5 = int(input('Digite um número:'))
    # imprime uma mensagem na tela com o resultado dos cálculos
    print('O maior número entre os 5 é:', maior(numero1,numero2,numero3,numero4,numero5))
    # imprime uma mensagem na tela com o resultado dos cálculos
    print('O menor é:', menor(numero1,numero2,numero3,numero4,numero5))
    # imprime uma mensagem na tela com o resultado dos cálculos
    print('E a média entre eles é:', media(numero1,numero2,numero3,numero4,numero5))
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()