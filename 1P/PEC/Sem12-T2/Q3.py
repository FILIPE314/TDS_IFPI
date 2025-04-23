def main():
    n = int(input('Digite um número: '))
    i = 0
    valorH = 0

    while i < n:
        i += 1
        valorH = valorH + (1 / i)  

    print(f'O valor de H com 4 (quatro) casas decimais é: {valorH:.4f}')

if __name__ == "__main__":
    main()