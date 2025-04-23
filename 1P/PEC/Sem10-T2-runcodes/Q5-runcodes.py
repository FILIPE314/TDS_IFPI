# função da estrutura de repetição
def repet():
    valor = float(input())
    # estrutura de repetição ou iteração
    for prestacao in range(24):
        prestacao += 1
        print(f'{prestacao}x de R$ {valor / prestacao:.2f}')
# função (main) que inicia e termina o programa
def main():
    repet()
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()