def ler_itens():
    lista = []
    while True:
        item = int(input('Digite o valor, use o zero(0) para encerrar: '))
        if item == 0: break
        lista.append(item)
    return lista

def contar(num, lista):
    cont = 0
    for i in lista:
        if num == i:
            cont += 1
    return cont

def main():
    lista = ler_itens()
    num = int(input('Qual número deseja verificar a quantidade de repetição: '))
    qntdNum = contar(num, lista) 
    print(f'A lista gerada é: {lista}')
    print(f'O número escolhido: {num}')
    print(f'O número escolhido se repete {qntdNum} vezes.')

if __name__ == "__main__":
    main()