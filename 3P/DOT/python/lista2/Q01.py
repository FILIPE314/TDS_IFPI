# 1) Faça um programa que grave uma lista de 100 elementos numéricos inteiros e: 
# a) Mostre a quantidade de números pares; 
# b) Grave uma lista somente com os números pares e mostre a lista; 
# c) Mostre a quantidade de números ímpares; 
# d) Grave uma lista somente com os números ímpares e mostre a lista.
# Reposta a)
def pares(list):
    quantidade_pares = 0
    for i in list:
        if i % 2 == 0:
            quantidade_pares += 1
    return f'Quantidade de números pares: {quantidade_pares}'
def main():
    lista = list(range(100))
    print(pares(lista))
if __name__ == '__main__':
    main()