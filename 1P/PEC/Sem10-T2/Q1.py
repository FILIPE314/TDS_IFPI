# função da estrutura de repetição
def repet():
    cancao = 0
    # estrutura de repetição ou iteração
    for cancao in range(250):
        print(cancao + 1,'bugs no software, pegue um deles e conserte...')
        cancao = cancao + 1
# função (main) que inicia e termina o programa
def main():
    repet()
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()