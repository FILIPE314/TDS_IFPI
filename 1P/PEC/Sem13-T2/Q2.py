def numeros100():
    lista = []
    for i in range(100):
        num = int(input(f'Digite o {i + 1}° número: '))
        lista.append(num)
    lista = sorted(lista)
    return lista

def lista_nova(lista):
    lista_nova = []
    for i in range(len(lista)):
        if i % 2 != 0:
            num_impar = lista[i] * 5
            lista_nova.append(num_impar)
        else:
            num_par = lista[i] * 3
            lista_nova.append(num_par)
    return lista_nova

def main():
    lista = numeros100()
    lista_alterada = lista_nova(lista)
    print(f'A nova lista onde os elementos de índice par são multiplicados por 3 e os elementos de índice ímpar são multiplicados com 5 é: \n{lista_alterada}')

if __name__ == "__main__":
    main()