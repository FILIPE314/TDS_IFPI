def ler_numeros(n):
    lista = []
    lista_par = []
    lista_impar = []
    for i in range(n):
        num = int(input(f'Digite o {i+1}° número: '))
        lista.append(num)
        if num % 2 == 0:
            lista_par.append(num)
        else:
            lista_impar.append(num)
    return lista, lista_par, lista_impar

def main():
    lista, lista_par, lista_impar = ler_numeros(20)
    print(f'Lista completa: {lista}')
    print(f'Lista dos números pares: {lista_par}')
    print(f'Lista dos números ímpares: {lista_impar}')

if __name__ == '__main__':
    main()