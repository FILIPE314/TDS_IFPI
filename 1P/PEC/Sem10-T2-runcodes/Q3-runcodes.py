# função da estrutura de repetição
def repet():
    # estrutura de repetição ou iteração
    for cancao in range(99, 251, 7):
        print(cancao,'bugs no software, pegue sete deles e conserte...')
        print('Tecle "Ctrl+F5"')
    print('Vamos fazer mais um café!')
# função (main) que inicia e termina o programa
def main():
    repet()
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()