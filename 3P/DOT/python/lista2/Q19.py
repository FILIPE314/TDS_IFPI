# 19) Ler duas listas: R de 5 elementos e S de 10 elementos. Gerar uma lista X de 15 elementos 
# cujas 5 primeiras posições contenham os elementos de R e as 10 últimas posições, os elementos 
# de S. Escrever a lista X.
from random import randint
def gerar_lista(r, s):
    x = []
    for i in range(len(r)):
        x.append(r[i])
    for i in range(len(s)):
        x.append(s[i])
    return f'\nLista gerada {x}\n'
def main():
    r = []
    s = []
    for i in range(16):
        if i < 5:
            r.append(randint(1, 10))
        if i > 5:
            s.append(randint(1, 10))
    print(f'Lista r: {r}\n \nLista s: {s}')
    while True:
        try:
            print(gerar_lista(r, s))
            break
        except:
            print(f'\nOps... Algo de errado não está certo, digite um valor válido!')
            break
if __name__ == '__main__':
    main()