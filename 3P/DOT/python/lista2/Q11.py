# 11) Faça um programa que alimente uma lista com um número de posições definidas pelo 
# usuário. 
# Esta lista deverá armazenar um conjunto de nomes em diferentes posições. 
# Crie um mecanismo para alimentar elementos da lista e pesquisar por um valor existente. 
# ======MENU======== 
# 1)Cadastar nome 
# 2)Pesquisar nome 
# 3)Listar todos os nome 
# 0)Sair do programa 
# ==================
# Digite sua escolha:
def menu(input_menu, lista, nome):
    if input_menu == 1:
        lista.append(nome)
        return f'...\nNome adicionado lista:{lista}'
    if input_menu == 2:
        for i in lista:
            if nome == i:
                return f'\nO nome {nome}, já existe na lista'
def main():
    lista = []
    while True:
        try:
            print(f'\nSegue abaixo um menu para escolher oque fazer em uma lista\n' + \
                  f'\n===========================MENU===========================\n' + \
                  f'1) Cadastar nome\n' + \
                  f'2) Pesquisar nome\n' + \
                  f'3) Listar todos os nome\n' + \
                  f'0) Sair do programa\n' + \
                  f'===========================================================\n')
            input_menu = int(input(f'Digite sua escolha: '))
            if input_menu == 1 or input_menu == 2:
                nome = input('Digite o nome que quer adicionar ou pesquisar: ')
                print(menu(input_menu, lista, nome))
                continue
            if input_menu == 3:
                print(f'Lista: {lista}')
            else:
                break
        except:
            print(f'\nOps... Algo de errado não está certo, digite um valor válido!')
if __name__ == '__main__':
    main()