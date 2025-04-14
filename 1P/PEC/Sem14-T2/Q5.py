def ler_itens(n):
    lista = []
    for i in range(n):
        item = int(input(f'Digite o valor do {i+1}° item: '))
        lista.append(item)
    return lista

def eliminar_repetidos(lista):
    lista_nova = []
    for i in range(len(lista)):
        if lista[i] not in lista_nova:
            lista_nova.append(lista[i])
    return lista_nova     

def unir(listaA, listaB):
    lista_unida = []
    for i in range(len(listaA)):
        lista_unida.append(listaA[i])
    for i in range(len(listaB)):
        lista_unida.append(listaB[i])

    return lista_unida

def main():
    qntdElementos = 10
    lista_A = ler_itens(qntdElementos)
    lista_B = ler_itens(qntdElementos)

    listaA_SemRepetidos = eliminar_repetidos(lista_A)
    listaB_SemRepetidos = eliminar_repetidos(lista_B)
    lista_unida = unir(listaA_SemRepetidos, listaB_SemRepetidos)
    listaUnida_SemRepetidos = eliminar_repetidos(lista_unida)

    print(f'A união das duas listas geradas, sem elemento repetido é:\n{listaUnida_SemRepetidos}')

if __name__ == '__main__':
    main()