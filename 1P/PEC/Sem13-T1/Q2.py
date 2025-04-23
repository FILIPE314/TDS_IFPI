def main():
    n = int(input('Digite o valor de n: '))
    lista = [0] * n
    print(f'Listas com zero: {lista}')

    lista = list(range(1, n + 1))
    print(f' Lista com números de 1 a n: {lista}')

    lista = []
    for i in range(n):
        lista.append(int(input(f'Digite o valor {i + 1}: ')))
    print(f'Lista com os valores lidos: {lista}')

    lista = []
    for i in range(n):
        lista.insert(0, int(input(f"Digite o valor {i + 1}: ")))
    print(f'Lista invertida dos valores lidos: {lista}')

if __name__ == "__main__":
    main()