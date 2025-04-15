# 3) Faça um programa que dada uma sequência de n números, imprimi-la na ordem inversa à da
# leitura.

from random import randint
# Função que gera uma lista aleatória com uma quantidade especificada de números, com intervalo de 1 a 10
def gera_lista(qtd_num):
    lista = []
    while len(lista) < qtd_num:
        x = randint(1, 10)
        if x not in lista:
            lista.append(x)
    return lista

#Função que recebe uma lista e retorna a mesma na ordem inversa
def lista_inversa(lista):
    lista_inversa = []
    # Loop que percorre a lista e adiciona os valores na ordem inversa em outra lista
    for i in range(len(lista)-1, -1, -1):
        lista_inversa.append(lista[i])    
    return lista_inversa   

def main():
    while True:
        lista_numeros = gera_lista(10)
        if type(lista_numeros) != str:
            lista_ordem_inversa = lista_inversa(lista_numeros)
            print(f"lista: {lista_numeros}\n\nLista na ordem inversa: {lista_ordem_inversa}")
            break
        else:
            print("Entrada inválida! a lista deve ser de números, tente novamente!")
if __name__=="__main__":
    main()
    