def ler_lista(n):
    lista = []
    for i in range(n):
        num = int(input(f'Digite o {i + 1}° número: '))
        lista.append(num)
    return lista

def intercalar(listaA, listaB):
    lista_c = []
    for i in range(len(listaA)): # ou len(listaB)
        lista_c.append(listaA[i])
        lista_c.append(listaB[i])
    return lista_c

def main():
    lista_A = ler_lista(25)
    lista_B = ler_lista(25)
    lista_C = intercalar(lista_A, lista_B)

    print(f'A lista A é: {lista_A}')
    print(f'A lista B é: {lista_B}')
    print(f'A lista intercalada entre A e B é: {lista_C}')

if __name__ == '__main__':
    main()