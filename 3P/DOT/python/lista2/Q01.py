# 1) Faça um programa que grave uma lista de 100 elementos numéricos inteiros e: 
# a) Mostre a quantidade de números pares; 
# b) Grave uma lista somente com os números pares e mostre a lista; 
# c) Mostre a quantidade de números ímpares; 
# d) Grave uma lista somente com os números ímpares e mostre a lista.
# Resposta a)
def pares(list):
    quantidade_pares = 0
    for i in list:
        if i % 2 == 0:
            quantidade_pares += 1
    return f'Quantidade de números pares: {quantidade_pares}\n'
# Resposta b)
def list_pares(list):
    todos_os_pares = []
    for i in list:
        if i % 2 == 0:
            todos_os_pares.append(i)
    return f'Aqui estão todos os pares {todos_os_pares}\n'
# Resposta c)
def list_impares(list):
    quantidade = 0
    for i in list:
        if i % 2 != 0:
            quantidade += 1
    return f'Quantidade de números ímpares: {quantidade}\n'
def main():
    # Letra a
    lista = list(range(100))
    print(pares(lista))
    # Letra b
    print(list_pares(lista))
    # Letra c
    print(list_impares(lista))
if __name__ == '__main__':
    main()