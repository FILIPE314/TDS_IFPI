def ler_numeros():
    lista = []
    cont = 0
    while True:
        num = int(input())
        if num == 0: break
        cont += 1
        lista.append(num)
    return lista

def soma_cumulativa(lista):
    nova_lista = []
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
        nova_lista.append(soma)
    return nova_lista

def main():
    lista = ler_numeros()
    lista_soma = soma_cumulativa(lista)

    print(lista_soma)

if __name__ == '__main__':
    main()