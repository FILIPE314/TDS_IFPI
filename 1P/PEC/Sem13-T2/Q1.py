def numerosInteiros():
    lista = []
    i = 0
    while True:
        num = int(input(f'Digite o {i + 1}° número: '))
        i += 1
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
    const = int(input('Digite o valor da constante: '))
    novaLista = multiplica_constante(lista, const)
    print(f'A nova lista onde cada valor da lista original é a multiplicado pelo valor da constante é:\n{novaLista}')

if __name__ == "__main__":
    main()