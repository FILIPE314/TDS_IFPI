def ler_itens(n):
    lista = []
    for i in range(n):
        item = int(input(f'Digite o valor do {i+1}° item: '))
        lista.append(item)
    return lista

def main():
    qtdNum = 10
    lista = ler_itens(qtdNum)

    qtd_negativo = 0
    soma_positivo = 0
    for i in range(qtdNum):
        if lista[i] < 0: 
            qtd_negativo += 1
        else:
            soma_positivo += lista[i]

    print(f'A lista gerada é: {lista}')
    print(f'A quantidade de valores negativos da lista é: {qtd_negativo}')
    print(f'A soma dos valores positivos: {soma_positivo}')


if __name__ == "__main__":
    main()