# função que calcula o preço do produto dependendo do quanto ele vale por quilos
def preco(valor_quilo, quilos):
    # condição que verifica se os valores são positivos
    if valor_quilo <= 0 or quilos <= 0:
        # imprime uma mensagem caso os valores não sejam positivos
        print('0.00')
    # condição contrária
    else:
        # variável da função
        x = valor_quilo * quilos
        # imprime o preço do produto
        print(f'{x:.2f}')
# função (main) que inicia o programa
def main():
    # variável que imprime uma mensagem na tela e armazena dados
    valor_quilo = float(input())
    # variável que imprime uma mensagem na tela e armazena dados
    quilos = float(input())
    # aciona a função
    preco(valor_quilo, quilos)
# complementar da função (main) só que essa encerra o programa
if __name__ == '__main__':
    main()