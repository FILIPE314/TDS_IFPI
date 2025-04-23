def main():
    
    lista = []
    n = int(input())
    for i in range(n):
        num = float(input())
        num = round(num, 4)
        lista.insert(0, num)
    print(lista)

    
    lista = []
    if n == 0: 
        print(lista)
        print('SEM NOTAS')
    else:
        for i in range(n):
            num = float(input())
            num = round(num, 1)
            lista.append(num)
        print(lista)
        media = sum(lista)/n
        print(f'{media:.1f}')

   
    lista = []
    lista_consoante = []
    count = 0

    for i in range(n):
        letra = input().strip()
        lista.append(letra)

    for i in range(n):
        if lista[i] in 'aeiouAEIOU': 
            count += 1
        else:
            lista_consoante.append(lista[i])
    print(count)
    print(lista_consoante)

if __name__ == '__main__':
    main()