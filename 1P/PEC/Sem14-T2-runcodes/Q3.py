def ler_itens(n):
    lista = []
    for i in range(n):
        item = int(input())
        lista.append(item)
    return lista

def eliminar_repetidos(lista):
    lista_nova = []
    for i in range(len(lista)):
        if lista[i] not in lista_nova:
            lista_nova.append(lista[i])
    return lista_nova     

def main():
    qtdNum = 20
    lista = ler_itens(qtdNum)
    lista_sem_repetidos = eliminar_repetidos(lista)
    print(lista_sem_repetidos)

if __name__ == '__main__':
    main()