def ler_itens(n):
    lista = []
    for i in range(n):
        item = int(input(f'Digite o valor do {i+1}° item: '))
        lista.append(item)
    return lista

def main():
    qtdNum = 10
    lista = ler_itens(qtdNum)
    maiorElemento = max(lista)
    indexMaiorElemento = lista.index(maiorElemento)

    print(f'A lista gerada é: {lista}')
    print(f'O maior elemento da lista é: {maiorElemento}')
    print(f'O index do maior elemento é: {indexMaiorElemento}')

if __name__ == "__main__":
    main()