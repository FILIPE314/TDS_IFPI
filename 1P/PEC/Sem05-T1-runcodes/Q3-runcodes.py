# função que calcula e retorna o valor do cálculo
def aumento1(preco, percentual):
    x = percentual * preco/100
    return preco + x
# função que calcula e retorna o valor do cálculo
def desconto1(preco, percentual):
    x = percentual * preco/100
    return preco - x
# função (main) que inicia e termina o programa
def main():
    # variáveis que imprimem uma informação na tela e armazenam dados
    preco = float(input().strip())
    percentual = float(input().strip())
    # guardando o resultado em variáveis
    aumento = aumento1(preco, percentual)
    desconto = desconto1(preco, percentual)
    # imprimindo o resultado na tela do computador do usuário
    print(f'{aumento:.2f}')
    print(f'{desconto:.2f}')
# complementar da função (main) essa encerra o programa 
if __name__=='__main__':
    main()