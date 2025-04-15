# 9) Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela
# uma lista Y. A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa.

#Função que recebe uma lista e retorna a mesma na ordem inversa
def lista_inversa(lista):
    lista_inversa = []
    # Loop que percorre a lista e adiciona os valores na ordem inversa em outra lista
    for i in range(len(lista)-1, -1, -1):
        lista_inversa.append(lista[i])    
    return lista_inversa   

def main():
    lista = []
    cont = 0
    print("-----------Digite uma lista de 05 números.-----------")
    while cont < 5:
        try:
            cont += 1
            valor = float(input("--> "))
            lista.append(valor)
        except:
            cont -= 1
            print("\nERRO: Entrada inválida, não podem haver valores vazios e nem strings, devem ser números!") 

    lista_ordem_inversa = lista_inversa(lista)
    print(f"\nlista: {lista}\n\nLista na ordem inversa: {lista_ordem_inversa}")            
if __name__=="__main__":
    main()
    