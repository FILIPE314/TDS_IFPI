def main():
    quantidade = int(input().strip())

    populacao = quantidade
    ano = 1600
    nascidos = 0
    mortos = 0

    while True:
        if populacao < (quantidade * (10/100)): break
        nascidos = populacao * (1/100)
        mortos = populacao * (6/100)
        populacao = populacao - mortos + nascidos

        print(f'{round(ano)},{round(nascidos)},{round(mortos)},{round(populacao)}')
        ano += 1

        nascidos = 0
        mortos = 0

if __name__ == '__main__':
    main()