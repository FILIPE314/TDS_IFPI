# 17) Ler uma lista W de 10 elementos, depois ler um valor V. Contar e escrever quantas vezes o 
# valor V ocorre na lista W e escrever também em que posições (índices) da lista W o valor V 
# aparece.
from random import randint 
def aparecer(w, v):
    vezes = 0
    posicoes = []
    for i in range(len(w)):
        if w[i] == v:
            vezes += 1
            posicoes.append(i)
    return f'\nO valor {v} apareceu {vezes}, nas posições {posicoes}\n'
def main():
    w = []
    v = randint(1, 10)
    for i in range(10):
        w.append(randint(1, 10))
    print(w)
    while True:
        try:
            print(aparecer(w, v))
            break
        except:
            print(f'\nOps... Algo de errado não está certo, digite um valor válido!')
            break
if __name__ == '__main__':
    main()