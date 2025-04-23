# 15) Ler uma lista D de 10 elementos. Criar uma lista E, com todos os elementos de D na ordem inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assimpor diante. Escrever todo a lista D e todo a lista E.

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
    print("-----------Digite uma lista de 10 elementos.-----------")
    while cont < 10:
        cont += 1
        valor = input("--> ").strip()
        # Confere se o valor é vazio
        if not valor:
            cont -= 1
            print("\nERRO: Entrada inválida, não podem haver valores vazios!")  
        else:
            lista.append(valor)
                        
    lista_ordem_inversa = lista_inversa(lista)
    print(f"\nlista: {lista}\n\nLista na ordem inversa: {lista_ordem_inversa}")
if __name__=="__main__":
    main()
    