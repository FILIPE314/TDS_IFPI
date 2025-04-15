# 14) Ler uma lista C de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0. Escrever a lista C modificada.

# Função que recebe uma lista e retorna uma cópia, substituindo os valores negativos por zero
def zera_negativo(lista):
    lista_copia = lista[:]
    for i in range(len(lista_copia)):
        if lista_copia[i] < 0:
            lista_copia[i] = 0
    return lista_copia

def main():
    lista = []
    cont = 0
    print("-----------Digite uma lista de 10 números inteiros.-----------")
    while cont < 10:
        cont += 1
        try:
            valor = int(input("--> "))
            lista.append(valor)
        except:
            cont -= 1
            print("\nERRO: Entrada inválida, não podem haver valores vazios, devem ser números!")
    lista_resultado = zera_negativo(lista)
    print(f"\nLista original: {lista}")
    print(f"\nLista modificada: {lista_resultado}")   
    
if __name__=="__main__":
    main()

