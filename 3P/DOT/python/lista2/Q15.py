# 15) Ler uma lista D de 10 elementos. Criar uma lista E, com todos os elementos de D na ordem 
# inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assim 
# por diante. Escrever todo a lista D e todo a lista E.
def contrario(sequencia):
    y = []
    for i in range(len(sequencia) - 1, - 1, - 1):
        y.append(sequencia[i])
    return f'\nSequência x aocontrario: {y}\n'
def main():
    x = list(range(20, 31))
    while True:
        try:
            print('\nSequencia x normal:', x)
            print(contrario(x))
            break
        except:
            print(f'\nOps... Algo de errado não está certo, digite um valor válido!')
if __name__ == '__main__':
    main()