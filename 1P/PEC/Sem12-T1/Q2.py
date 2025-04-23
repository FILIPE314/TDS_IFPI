def main():
    precoAtual = float(input('Digite o preço atual de um carro: '))

    valorPoupanca = 10000
    valorCarro = precoAtual

    mes = 0
    taxaPoupanca = 0.007
    taxaCarro = 0.004

    while valorPoupanca < valorCarro:
        mes += 1
        valorPoupanca += taxaPoupanca * valorPoupanca 
        valorCarro += taxaCarro * valorCarro

    print(f'Em {mes} meses você terá dinheiro suficiente para comprar o carro à vista!!')

if __name__ == "__main__":
    main()