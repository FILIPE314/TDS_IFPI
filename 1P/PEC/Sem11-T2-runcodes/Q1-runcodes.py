def main():
    num = 0
    soma = 0

    while True:
        num = int(input().strip())
        if num == 0: break
        soma = soma + num

    print(soma)

if __name__ == '__main__':
    main()