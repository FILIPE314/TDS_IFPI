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
    deposito = float(input().strip())
    taxa = float(input().strip())

    print(f'{dobro(deposito, taxa)}')

if __name__ == '__main__':
    main()