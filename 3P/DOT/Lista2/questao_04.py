# 4) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
# a) O maior elemento da lista e em que posição esse elemento se encontra;
# b) O menor elemento da lista e em que posição esse elemento se encontra.

from random import randint
# Função que gera uma lista aleatória com uma quantidade especificada de números, com intervalo de 1 a 50
def gera_lista(qtd_num):
    lista = []
    while len(lista) < qtd_num:
        x = randint(1, 50)
        if x not in lista:
            lista.append(x)
        continue
    return lista

# Função para encontrar o maior item de uma lista, retorna a posição e o valor do maior item
def posicao_maximo(lista):
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    return lista.index(maior)+1, maior 

# Função para encontrar o menor item de uma lista, retorna a posição e o valor do menor item    
def posicao_minimo(lista):
    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i
    return lista.index(menor)+1, menor 
    
def main():
    while True:
        numeros = gera_lista(15)
        if type(numeros) != str:
            posicao_maior, maior = posicao_maximo(numeros)
            posicao_menor, menor = posicao_minimo(numeros)
            
            print(f'''\nLista: {numeros}
        \nO maior elemento é: {maior}, está na posição {posicao_maior}.
        \nO menor elemento é: {menor}, está na posição {posicao_menor}.''')
            break
        else:
            print("Entrada inválida! a lista deve ser de números, tente novamente!")
if __name__=="__main__":
    main()
