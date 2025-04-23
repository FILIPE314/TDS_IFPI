# função que calcula o preço de um carro novo
def car_new(custo):
    # calculando o preço do carro com aumento de 28% e outro aumento de 45%
    preco1 = custo + (custo * 0.28)
    preco2 = preco1 + (custo * 0.45)
    # imprimindo o preço do carro novo com os dois aumentos
    print(f'R$ {preco2:.2f}')
# função (main) que inicia o programa
def main():
    # variável que armazena o custo inicial do carro
    custo = float(input())
    # calculando e imprimindo o preço do carro novo
    car_new(custo)
# complementar da função (main) só que essa encerra o programa
if __name__=='__main__':
    main()