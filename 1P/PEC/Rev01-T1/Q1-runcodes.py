# função que calcula o troco da operação
def troco(preco, pagamento):
    # condição da função
    if preco < pagamento:
        # variável da função
        troco = pagamento - preco
        # imprime o valor formatado
        print(f'{troco:.2f}')
    # outra condição
    elif preco == pagamento:
        # imprime esse resultado caso seja essa a condição
        print('0.00')
    # condição contrária
    else:
        # imprime esse resultado caso seja essa a condição
        print('Pagamento Insuficiente')
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    preco = float(input())
    # variável que imprime uma informação na tela e armazena dados
    pagamento = float(input())
    # chama a função
    troco(preco, pagamento)
# complementar da função (main) essa encerra o programa
if __name__ == '__main__':
    main()