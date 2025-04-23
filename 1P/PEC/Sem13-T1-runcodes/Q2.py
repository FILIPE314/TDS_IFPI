def main():
    n = int(input())
    lista = [0] * n
    print(lista)
    lista = list(range(1, n + 1))
    print(lista)
    lista = []
    for i in range(n):
        lista.append(int(input()))
    print(lista)
    lista = []
    for i in range(n):
        lista.insert(0, int(input()))
    print(lista)

if __name__ == "__main__":
    main()