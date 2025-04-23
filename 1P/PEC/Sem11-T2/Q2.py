def main():
    num = 0
    soma = 0
    maior = 0
    menor = 0

    contador = 0

    while True:
        num = int(input('Insira um número').strip())
        if num == 0: break
        if num > maior: maior = num
        if menor == 0: menor = num
        if num > 0 and num < menor: menor = num

        soma = soma + num
        contador = contador + 1

    print('A quantidade de números é:', contador)
    print(f'A média aritmética é: {soma/contador:.2f}')
    print('O menor número é:', menor)
    print('O maior número é:', maior)

if __name__ == '__main__':
    main()