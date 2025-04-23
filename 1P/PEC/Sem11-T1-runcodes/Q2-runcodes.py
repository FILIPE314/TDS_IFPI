def main():
    num = 0
    contador = 0
    soma = 0

    while True:
        num = int(input().strip())
        if num == 0: break
        soma = soma + num
        contador = contador + 1

    print(f'{soma/contador:.2f}')

if __name__ == '__main__':
    main()