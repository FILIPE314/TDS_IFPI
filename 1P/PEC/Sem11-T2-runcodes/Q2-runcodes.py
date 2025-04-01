def main():
    num = 0
    soma = 0
    maior = 0
    menor = 0

    contador = 0

    while True:
        num = int(input().strip())
        if num == 0: break
        if num > maior: maior = num
        if menor == 0: menor = num
        if num > 0 and num < menor: menor = num

        soma = soma + num
        contador = contador + 1

    print(contador)
    print(f'{soma/contador:.2f}')
    print(menor)
    print(maior)

if __name__ == '__main__':
    main()