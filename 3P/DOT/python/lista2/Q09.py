# 9) Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela 
# uma lista Y. A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa.
def contrario(sequencia):
    y = []
    for i in range(len(sequencia) - 1, - 1, - 1):
        y.append(sequencia[i])
    return f'\nSequência x aocontrario: {y}\n'
def main():
    x = list(range(20, 26))
    while True:
        try:
            print('\nSequencia x normal:', x)
            print(contrario(x))
            break
        except:
            print(f'\nOps... Algo de errado não está certo, digite um valor válido!')
if __name__ == '__main__':
    main()