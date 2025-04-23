def main():
    num = 0
    maior = 0
    menor = 0

    while True:
        num = int(input().strip())
        if num == 0: break
        if num > maior: maior = num
        if menor == 0: menor = num
        if num > 0 and num < menor: menor = num

    print(maior)
    print(menor)

if __name__ == '__main__':
    main()