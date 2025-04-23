# função que calcula o desconto
def desconto(valor):
    # variável local
    percentagem = valor * 0,09
    # variável local
    percentagem2 = valor - percentagem
    # retorna o valor calculado
    return percentagem2
# função que calcula o valor em prestações sem juros
def prestacao(valor):
    # retorna o valor calculado
    return valor / 5
# função que calcula o valor com juros dividido em 10 prestações
def juros(valor):
    # variável local
    juros = valor * 0,17
    # variável local
    juros2 = valor + juros
    # retorna o valor calculado
    return juros2 / 10
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazenam dados
    valor = float(input('Digite o valor de um produto e iremos calcular o seu preço com desconto, o valor da prestação dividido em 5 vezes e o valor acrescentado de juros e dividido em 10 vezes:'))
    # imprime uma mensagem na tela com o resultado dos cálculos
    print('O valor de seu produto com 9% de desconto:',desconto(valor))
    # imprime uma mensagem na tela com o resultado dos cálculos
    print('O valor do seu produto dividido em 5 prestações:',prestacao(valor))
    # imprime uma mensagem na tela com o resultado dos cálculos
    print('O valor do seu produto acrescentado em juros e dividido em 10 prestações:',juros(valor))
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()