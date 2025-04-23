def dobro(deposito, taxa):
    i = 1
    capital = deposito
    while True:
        # juros compostos
        capital = deposito * (taxa/100 + 1) ** i
        if capital >= deposito * 2: break
        i+=1
    return i

def main():
    deposito = float(input('Insira o valor do depósito: ').strip())
    taxa = float(input('Insira o valor da taxa: ').strip())

    print(f'O valor irá dobrar em: {dobro(deposito, taxa)} ano.')

if __name__ == '__main__':
    main()