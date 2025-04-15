# 5) Faça um programa que leia duas listas de 10 elementos numéricos cada uma e intercale os
# elementos deste em uma outra lista de 20 elementos.

from random import randint

# Função que gera uma lista aleatória com uma quantidade especificada de números, com intervalo de 1 a 50
def gera_lista(qtd_num):
    lista = []
    while len(lista) < qtd_num:
        x = randint(1, 50)
        if x not in lista:
            lista.append(x)
    return lista

# Função que intercala os itens de duas listas e retorna uma nova lista conjugada 
def intercala_lista(lista_1, lista_2):
    nova_lista = []
    for i in range(len(lista_1)):
        nova_lista.append(lista_1[i])
        nova_lista.append(lista_2[i])
    return nova_lista

def main():
    while True:
        lista_1 = gera_lista(10)
        lista_2 = gera_lista(10)
        if type(lista_1) and type(lista_2) != str: 
            lista_conjugada = intercala_lista(lista_1, lista_2)
    
            print(f'''\nLista 1: {lista_1}
            \nlista 2: {lista_2}
            \nLista conjugada: {lista_conjugada}''')
            break
        else:
            print("Entrada inválida! a lista deve ser de números, tente novamente!")
if __name__=="__main__":
    main()
