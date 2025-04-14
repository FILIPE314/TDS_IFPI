def ler_numeros(n):
    lista = []
    lista_par = []
    lista_impar = []
    for i in range(n):
        num = int(input())
        lista.append(num)
        if num % 2 == 0:
            lista_par.append(num)
        else:
            lista_impar.append(num)
    return lista, lista_par, lista_impar

def main():
    lista, lista_par, lista_impar = ler_numeros(20)
    print(lista)
    print(lista_par)
    print(lista_impar)

if __name__ == '__main__':
    main()