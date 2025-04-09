# 14) Ler uma lista C de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0. Escrever a lista C modificada.
from random import *
def trocar_negativo(list):
    for i in range(len(list)):
        if list[i] < 0:
            list[i] = 0
    return f'\nLista modificada com números negativos igual a zero:\n {list}'
def main():
    list = []
    for i in range(10):
        a = randint(-5, 5)
        list.append(a)
    print(f'Lista com números negativos:\n {list}')
    while True:
        try:
            print(trocar_negativo(list))
            break
        except:
            print(f'\nOps... Algo de errado não está certo, digite um valor válido!')
            break
if __name__ == '__main__':
    main()