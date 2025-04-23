# função que calcula o troco da operação
def troco(preco, pagamento):
    # condição da função
    if preco < pagamento:
        # variável da função
        troco = pagamento - preco
        # imprime o valor formatado
        print(f'Seu troco é {troco:.2f} reais')
    # outra condição
    elif preco == pagamento:
        # imprime esse resultado caso seja essa a condição
        print('Seu troco é 0.00 reais')
    # condição contrária
    else:
        # imprime esse resultado caso seja essa a condição
        print('Pagamento Insuficiente')
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    preco = float(input('Para saber o valor do seu troco, digite o preço do produto:'))
    # variável que imprime uma informação na tela e armazena dados
    pagamento = float(input('Agora digite o quanto você pagou:'))
    # chama a função
    troco(preco, pagamento)
# complementar da função (main) essa encerra o programa
if __name__ == '__main__':
    main()