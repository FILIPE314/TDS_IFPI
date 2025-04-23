def ler_itens():
    lista = []
    while True:
        item = int(input())
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

    print(lista)
    print(numItens)
    print(listInvert)
    print(numMenor)
    print(numMaior)
    print(listSoma)

if __name__ == "__main__":
    main()