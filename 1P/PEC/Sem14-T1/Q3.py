def ler_itens(n):
    lista = []
    for i in range(n):
        item = int(input(f'Digite o {i + 1}° valor: '))
        lista.append(item)
    return lista

def somaListas(listaA, listaB):
    lista_C = []
    for i in range(len(listaA)):
        soma = listaA[i] + listaB[i]
        lista_C.append(soma)
    return lista_C       

def main():
    qntdElemento = 20
    lista_A = ler_itens(qntdElemento)
    lista_B = ler_itens(qntdElemento)
    lista_C = somaListas(lista_A, lista_B)
    print(f'A primeira lista gerada é:{lista_A}')
    print(f'A segunda lista gerada é:{lista_B}')
    print(f'A soma das listas geradas é:{lista_C}')

if __name__ == '__main__':
    main()