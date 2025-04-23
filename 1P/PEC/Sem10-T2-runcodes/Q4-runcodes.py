# função da estrutura de repetição
def repet():
    # estrutura de repetição ou iteração
    for cancao in range(99, 10, -11):
        print(cancao,'bugs no software, pegue onze deles e conserte...')
        print('Tecle "Ctrl+F5"')
    print('Sem erros no software! Está estabilizado!')
# função (main) que inicia e termina o programa
def main():
    repet()
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()