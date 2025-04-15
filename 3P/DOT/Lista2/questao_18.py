# 18) Ler uma lista X de 10 elementos. A seguir copiar todos os valores negativos da lista X para uma lista R, sem deixar elementos vazios entre os valores copiados. Escrever as listas X e R.

# Função que copia os valores negativos de uma lista para outra separada, retornando a nova lista
def retira_negativos(lista):
    nova_lista = []
    for i in range(len(lista)):
        if lista[i] < 0:
            nova_lista.append(lista[i])
    return nova_lista

def main():
    lista_numeros = []
    cont = 0
    print("-----------Digite uma lista de 10 números.-----------")
    while cont < 10:
        try:
            cont += 1
            valor = int(input("--> "))
            lista_numeros.append(valor)
        except:
            cont -= 1
            print("\nERRO: Entrada inválida, não podem haver valores vazios, devem ser números!")  
                            
    nova_lista = retira_negativos(lista_numeros)
    print(f"Lista original (x): {lista_numeros}")
    # Confere se a lista está vazia
    if not nova_lista:
        print("\nA lista X não possui valores negativos!")
    else:   
        print(f"\nLista X sem valores negativos: {nova_lista}")
if __name__=="__main__":
    main()