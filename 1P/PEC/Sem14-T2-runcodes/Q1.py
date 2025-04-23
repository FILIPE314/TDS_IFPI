def ler_itens(n):
    lista = []
    for i in range(n):
        item = int(input())
        lista.append(item)
    return lista

def main():
    qtdNum = 10
    lista = ler_itens(qtdNum)
    maiorElemento = max(lista)
    indexMaiorElemento = lista.index(maiorElemento)

    print(lista)
    print(maiorElemento)
    print(indexMaiorElemento)

if __name__ == "__main__":
    main()