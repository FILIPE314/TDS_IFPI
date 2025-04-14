# função que calcula e retorna o valor do cálculo
def aumento1(preco, percentual):
    return preco + percentual
# função que calcula e retorna o valor do cálculo
def desconto1(preco, percentual):
    return preco - percentual
# função (main) que inicia e termina o programa
def main():
    # variáveis que imprimem uma informação na tela e armazenam dados
    preco = float(input('Para saber o preço de um produto acrescido de um percentual ou descontado de um percentual, digite o preço do produto:'))
    percentual = float(input('Agora aqui digite o percentual que deseja:'))
    # guardando o resultado em variáveis
    aumento = aumento1(preco, percentual)
    desconto = desconto1(preco, percentual)
    # imprimindo o resultado na tela do computador do usuário
    print(f'O preço acrescido do percentual:{aumento:.2f}')
    print(f'O preço com desconto:{desconto:.2f}')
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()