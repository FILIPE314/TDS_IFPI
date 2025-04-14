# 11) Faça um programa que alimente uma lista com um número de posições definidas pelo
# usuário.
# Esta lista deverá armazenar um conjunto de nomes em diferentes posições.

# Crie um mecanismo para alimentar elementos da lista e pesquisar por um valor existente.
# ==== =MENU========
# 1)Cadastar nome
# 2)Pesquisar nome
# 3)Listar todos os nome
# 0) Sair do programa
# ——————–
# Digite sua escolha:_

def main():    
    try:
        num_posicoes = int(input("\nDigite a quantidade de posições da lista: "))
        lista = []
        
        while True:
            print(f'''\n{'='*10} MENU {'='*10}
1) Cadastrar nome
2) Pesquisar nome
3) Listar todos os nomes
0) Sair do programa''')
            opcao = int(input("\nDigite sua escolha: "))
            if opcao == 1:
                nome = input("\nDigite o nome que deseja adicionar: ")
                if len(lista) >= num_posicoes:
                    print("\nERRO: A lista já alcançou a quantidade máxima!")
                else:
                    lista.append(nome)      
                                  
            elif opcao == 2:
                nome = input("\nDigite o nome que deseja cadastrar: ")
                if nome in lista:
                    print(f"\nO nome {nome} ESTÁ na lista, na posição {lista.index(nome)+1}.")
                else:
                    print(f"\nO nome {nome} NÃO está na lista.")
                    
            elif opcao == 3:
                if len(lista) == 0:
                    print("\nA lista está vazia")
                else:
                    print(f"\nLISTA DE NOMES: {lista}")
                    
            elif opcao == 0:
                print("\nEncerrando programa...")                
                break
            else:
                print("\nERRO: Digite uma opção válida!")                
    except ValueError:
        print("\nERRO: Digite um valor numérico para a quantidade de posições, tente novamente!")
        main()
if __name__=="__main__":
    main()
