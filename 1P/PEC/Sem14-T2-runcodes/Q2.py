def ler_itens(n):
    lista = []
    for i in range(n):
        item = int(input())
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

    print(lista)
    print(qtd_negativo)
    print(soma_positivo)


if __name__ == "__main__":
    main()