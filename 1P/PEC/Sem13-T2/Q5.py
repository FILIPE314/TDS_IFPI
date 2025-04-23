def ler_valores(n):
    lista = []
    for i in range(n):
        valor = input(f'Digite o {i + 1} valor: ').strip()  
        try:
            num = int(valor)
            lista.append(num)
        except ValueError:
            try:
                num = float(valor)
                lista.append(num)
            except ValueError:
                lista.append(valor)
    return lista

def esta_ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True # Só False se pelo menos um for menor que o próximo, True: valor PADRÃO

def main():
    n = int(input('Digite o valor da constante: '))
    lista = ler_valores(n)
    conferencia = esta_ordenada(lista)

    if conferencia:
        print('LISTA ORDENADA')
    else:
        print('LISTA NÃO ORDENADA')

if __name__ == '__main__':
    main()