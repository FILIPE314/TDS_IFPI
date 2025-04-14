def ler_conjuntos(n):
    lista = []
    for i in range(n):
        item = int(input(f'Digite o valor do {i+1}° item: '))
        lista.append(item)
    return lista

def produto_escalar(listaA, listaB):
    soma = 0
    for i in range(len(listaA)):
        produto = listaA[i] * listaB[i]
        soma += produto
    return soma 

def main():
    qtdElemntos = 5
    lista_A = ler_conjuntos(qtdElemntos)
    lista_B = ler_conjuntos(qtdElemntos)
    resultado = produto_escalar(lista_A, lista_B)

    print(f'A primeira lista gerada é {lista_A}')
    print(f'A segunda lista gerada é {lista_B}')

    expressao = ''
    for i in range(qtdElemntos):
        if i == qtdElemntos - 1:
            expressao += f'({lista_A[i]} x {lista_B[i]}) '
        else:
            expressao += f'({lista_A[i]} x {lista_B[i]}) + '

    print(f'{expressao}= {resultado}')


if __name__ == '__main__':
    main()