def ler_itens():
    lista = []
    while True:
        item = int(input('Digite o valor, use o zero(0) para encerrar:'))
        if item == 0: break
        lista.append(item)
    return lista

def comprimento(lista):
    cont = 0
    for i in lista:
        cont += 1
    return cont

def inverter(lista):
    lista_invertida = []
    for i in lista:
        lista_invertida.insert(0, i)
    return lista_invertida

def minimo(lista):
    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i      
    return menor

def maximo(lista):
    maior = 0
    for i in lista:
        if i > maior:
            maior = i
    return maior

def soma(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

def main():
    lista = ler_itens()
    numItens = comprimento(lista)
    listInvert = inverter(lista)
    numMenor = minimo(lista)
    numMaior = maximo(lista)
    listSoma = soma(lista)

    print(f'A lista gerada é: {lista}')
    print(f'A quantidade de elementos que tem na lista é: {numItens}')
    print(f'A lista invertida é: {listInvert}')
    print(f'O menor numero da lista é: {numMenor}')
    print(f'O maior numero da lista é: {numMaior}')
    print(f'O resultado da soma dos elementos da lista é: {listSoma}')

if __name__ == "__main__":
    main()