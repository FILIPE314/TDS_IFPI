# 18) Ler uma lista X de 10 elementos. A seguir copiar todos os valores negativos da lista X para 
# uma lista R, sem deixar elementos vazios entre os valores copiados. Escrever as listas X e R. 
from random import *
def copiar_negativo():
    x = [-5, 0, 2, -5, 0, -2, 5, -5, -1, 5]
    r = []
    for i in x[:]:
        if i < 0:
            r.append(i)
            x.remove(i)
    return f'\nLista com números inteiros:\n {x}\n' + \
           f'\nLista com números negativos:\n {r}\n'
def main():
    while True:
        try:
            print(copiar_negativo())
            break
        except:
            print(f'\nOps... Algo de errado não está certo, digite um valor válido!')
            break
if __name__ == '__main__':
    main()