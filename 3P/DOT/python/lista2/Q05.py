# 5)  Faça  um  programa  que  leia  duas  listas  de  10  elementos  numéricos  cada  um  e  intercale  os 
# elementos deste em uma outra lista de 20 elementos.
def intercalar(list1, list2):
    lista_intercalada = []
    for i in range(len(list1)):
        num = list1[i]
        lista_intercalada.append(num)
        if i == list2[i]:
            lista_intercalada.append(list2[i])
    return f'As duas listas intercaladas: {lista_intercalada}'
def main():
    lista1 = list(range(11, 21))
    lista2 = list(range(10))
    while True:
        try:
            print('\nExemplo de lista intercalada\n')
            print(f'Listas:\n {lista1}\n {lista2}\n')
            print(intercalar(lista1, lista2))
            break
        except:
            print(f'\nOps... Algo de errado não está certo, digite um valor válido!')
if __name__ == '__main__':
    main()