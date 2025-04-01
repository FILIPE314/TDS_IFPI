def main():
    num = int(input('Digite um número: '))
    fatorial = 1
    count = num

    while count > 0:
        fatorial = fatorial * count
        count -= 1
    print(f'O fatorial do número lido é: {fatorial}')
if __name__ == "__main__":
    main()