# 16) Ler uma lista X de 10 elementos inteiros e positivos. Criar uma lista Y da seguinte forma: os 
# elementos de Y com índice par receberão os respectivos elementos de X divididos por 2; os 
# elementos com índice ímpar receberão os respectivos elementos de X multiplicados por 3. Escrever as listas X e Y.
from random import randint
def criar_lista(x):
    y = []
    for i in range(len(x)):
        if i % 2 == 0:
            y.append(x[i] / 2)
        if i % 2 != 0 and i % 2 != 0:
            y.append(x[i] * 3)
    return f'Lista modificada {y}\n'
def main():
    x = []
    for i in range(10):
        x.append(randint(-10, 10))
    print(f'\nLista normal {x}\n')
    while True:
        try:
            print(criar_lista(x))
            break
        except:
            print(f'\nOps... Algo de errado não está certo, digite um valor válido!')
            break
if __name__ == '__main__':
    main()