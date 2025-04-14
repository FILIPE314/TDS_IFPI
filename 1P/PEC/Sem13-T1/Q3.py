def main():
    lista = []
    n = int(input())
    for i in range(n):
        num = float(input())
        num = round(num, 4)
        lista.insert(0, num)
    print(f'Lista invertida dos valores lidos: {lista}')

    lista = []
    if n == 0: 
        print(f'Lista das notas lidas: {lista}')
        print('SEM NOTAS')
    else:
        for i in range(n):
            num = float(input())
            num = round(num, 1)
            lista.append(num)
        print(f'Lista das notas lidas: {lista}')
        media = sum(lista)/n
        print(f'A média das notas lidas: {media:.1f}')

    lista = []
    lista_consoante = []
    count = 0

    for i in range(n):
        letra = input(f'Digite a {i + 1}° letra: ').strip()
        lista.append(letra)

    for i in range(n):
        if lista[i] in 'aeiouAEIOU': 
            count += 1
        else:
            lista_consoante.append(lista[i])
    print(f'Total de vogais: {count}')
    print(f'Lista das consoantes: {lista_consoante}')

if __name__ == '__main__':
    main()