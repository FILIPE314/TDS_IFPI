def ler_itens():
    lista = []
    while True:
        item = int(input())
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
    num = int(input())
    qntdNum = contar(num, lista) 
    print(lista)
    print(num)
    print(qntdNum)

if __name__ == "__main__":
    main()