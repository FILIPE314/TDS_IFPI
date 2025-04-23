# função que calcula o total que será gasto em um tipo de produto (maçã)
def maca(preco):
    # retorna o valor calculado
    return preco * 3
# função que calcula o total que será gasto em um tipo de produto (banana)
def banana(preco2):
    # retorna o valor calculado
    return preco2 * 2
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    preco = float(input('Digite aqui um valor para uma maçã para que possa ser calculado quanto foi o custo total:'))
    # variável que imprime uma informação na tela e armazena dados
    preco2 = float(input('Digite aqui um valor para uma banana para que possa ser calculado quanto foi o custo total:'))
    # imprime uma mensagem(formatada) na tela com o resultado dos cálculos
    print(f'O gasto total foi de: R${maca(preco) + banana(preco2):.2f}')
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()