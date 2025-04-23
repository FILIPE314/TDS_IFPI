# 1) Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
# a) Mostre a quantidade de números pares;
# b) Grave uma lista somente com os números pares e mostre a lista;
# c) Mostre a quantidade de números ímpares;
# d) Grave uma lista somente com os números ímpares e mostre a lista.
from random import randint

# Função que gera uma lista aleatória com uma quantidade especificada de números, com intervalo de 1 a 100
def gera_lista(qtd_num):
    lista = []
    for i in range(qtd_num):
        x = randint(1, 100)
        if x not in lista:
            lista.append(x)
    return lista

# Funções para determinar se é par
def eh_par(n):
    return n % 2 == 0

# Função que pega uma lista de números e retorna na sequencia uma lista dos números pares, lista dos números impares, quantidade de números pares e quantidade de números ímpares
def qtd_pares_impares(lista_numeros):
    # Listas que guardam os números separados
    num_pares = []
    num_impares = []
    # Contadores de números pares e ímpares
    qtd_par = 0
    qtd_impar = 0
    
    for i in lista_numeros:
        if eh_par(i):
            num_pares.append(i)
            qtd_par += 1
        else:
            num_impares.append(i)
            qtd_impar += 1
    return num_pares, num_impares, qtd_par, qtd_impar

def main():
    while True:
        numeros = gera_lista(100)
        if type(numeros) != str: 
            numeros_pares, numeros_impares, qtd_pares, qtd_impares = qtd_pares_impares(numeros)
        
            print(f'''{'='*20} lista: {numeros} {'='*20}
                \nA lista possui {qtd_pares} números pares!
            \nNúmeros pares: {numeros_pares}
                \nA lista possui {qtd_impares} números ímpares!
            \nNúmeros ímpares: {numeros_impares}''')
            break
        else:
            print("Entrada inválida! a lista deve ser de números, tente novamente!")
if __name__=="__main__":
    main()
