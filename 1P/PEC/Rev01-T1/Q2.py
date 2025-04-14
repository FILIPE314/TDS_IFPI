# função que calcula o preço do produto dependendo do quanto ele vale por quilos
def preco(valor_quilo, quilos):
    # condição que verifica se os valores são positivos
    if valor_quilo <= 0 or quilos <= 0:
        # imprime uma mensagem caso os valores não sejam positivos
        print('Valor Incorreto')
    # condição contrária
    else:
        # variável da função
        x = valor_quilo * quilos
        # imprime o preço do produto
        print(f'Você pagara {x:.2f} reais')
# função (main) que inicia o programa
def main():
    # variável que imprime uma mensagem na tela e armazena dados
    valor_quilo = float(input('Para saber quanto você pagara em um produto medido em quilos, digite quanto ele vale por quilo:'))
    # variável que imprime uma mensagem na tela e armazena dados
    quilos = float(input('Agora digite quantos quilos o produto tem:'))
    # aciona a função
    preco(valor_quilo, quilos)
# complementar da função (main) só que essa encerra o programa
if __name__ == '__main__':
    main()