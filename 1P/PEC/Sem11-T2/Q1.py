def main():
    num = 0
    soma = 0

    while True:
        num = int(input('Insira um número').strip())
        if num == 0: break
        soma = soma + num

    print('A soma de todos os números é:', soma)

if __name__ == '__main__':
    main()