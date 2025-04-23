def numerosInteiros():
    lista = []
    while True:
        num = int(input())
        if num == 0: break
        lista.append(num)
    return lista    

def multiplica_constante(lista, const):
    novaLista = []
    for i in range(len(lista)):
        num = lista[i] * const
        novaLista.append(num)
    return novaLista

def main():
    lista = numerosInteiros()
    const = int(input())
    novaLista = multiplica_constante(lista, const)
    print(novaLista)

if __name__ == "__main__":
    main()