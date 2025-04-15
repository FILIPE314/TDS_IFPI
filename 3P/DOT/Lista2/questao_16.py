#16) Ler uma lista X de 10 elementos inteiros e positivos. Criar uma lista Y da seguinte forma: os elementos de Y com índice par receberão os respectivos elementos de X divididos por 2; os elementos com índice ímpar receberão os respectivos elementos de X multiplicados por 3. Escrever as listas X e Y.

# Função que cria uma lista baseada em outra, com uma formula para criação de cada elemento, retornando no final a nova lista
def modifica_lista(lista):
    lista_modificada = []
    for i in range(len(lista)):
        if i % 2 == 0:
            lista_modificada.append(lista[i] / 2)
        else:
            lista_modificada.append(lista[i]*3)
    return lista_modificada

def main():
    lista = []
    cont = 0
    print("-----------Digite uma lista de 10 números inteiros e positivos.-----------")
    while cont < 10:
        cont += 1
        try:
            valor = int(input("--> "))
            lista.append(valor)
        except:
            cont -= 1
            print("\nERRO: Entrada inválida, digite apenas números inteiros!")
    nova_lista = modifica_lista(lista)
    print(f"\nLista original (X): {lista}")
    print(f"\nLista modificada (Y): {nova_lista}")  
    
if __name__=="__main__":
    main()
