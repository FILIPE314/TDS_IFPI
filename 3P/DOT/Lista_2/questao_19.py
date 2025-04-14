# 19) Ler duas listas: R de 5 elementos e S de 10 elementos. Gerar uma lista X de 15 elementos cujas 5 primeiras posições contenham os elementos de R e as 10 últimas posições, os elementos de S. Escrever a lista X.

def main():
    lista_r = []
    lista_s = []
    # Faz a leitura dos valores da lista (R) de 05 elementos
    cont_1 = 0
    print("-----------Digite uma lista de 5 elementos.-----------")
    while cont_1 < 5:
        cont_1 += 1
        valor = input("--> ").strip()
        # Confere se o valor é vazio
        if not valor:
            cont_1 -= 1
            print("\nERRO: Entrada inválida, não podem haver valores vazios!")  
        else:
            lista_r.append(valor)
    
    # Faz a leitura dos valores da lista (S) de 10 elementos
    cont_2 = 0
    print("\n-----------Digite uma lista de 10 elementos.-----------")
    while cont_2 < 10:
        cont_2 += 1
        valor = input("--> ").strip()
        # Confere se o valor é vazio
        if not valor:
            cont_2 -= 1
            print("\nERRO: Entrada inválida, não podem haver valores vazios!")  
        else:
            lista_s.append(valor)
            
    lista_x = lista_r + lista_s
    print(f"\nLista 'R': {lista_r}") 
    print(f"\nLista 'S': {lista_s}") 
    print(f"\nLista combinada (X): {lista_x}")             
if __name__=="__main__":
    main()