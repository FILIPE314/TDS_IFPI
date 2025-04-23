def main():
    num = 0
    maior = 0
    menor = 0

    while True:
        num = int(input('Insira um número: ').strip())
        if num == 0: break
        if num > maior: maior = num
        if menor == 0: menor = num
        if num > 0 and num < menor: menor = num

    print('O maior número é:', maior)
    print('O menor número é:', menor)

if __name__ == '__main__':
    main()