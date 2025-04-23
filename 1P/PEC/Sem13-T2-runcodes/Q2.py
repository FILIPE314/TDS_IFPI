def numeros100():
    lista = []
    for i in range(100):
        num = int(input())
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
    print(lista_alterada)

if __name__ == "__main__":
    main()