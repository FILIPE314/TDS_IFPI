# função condicional que imprime um resultado
def ler(nome):
    # imprime uma mensagem na tela quando a função é acionada
    return len(nome)
# função condicional que retorna um resultado dependendo da resposta do ususário
def opcao2(c_ou_s):
    if c_ou_s == '1':
        # variável local que contém uma entrada para o usuário dependendo da sua escolha
        nome_c = input().strip()
        ler2 = len(nome_c)
        # retorna o resutado caso seja esssa opção
        return ler2
    # condicional(falsa ou contrária)
    else:
        # imprime uma mensagem na tela quando a função é acionada caso seja a opção
        return 0
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    nome = input().strip()
    # variável que imprime uma informação na tela e armazena dados
    c_ou_s = input().strip()
    # imprime uma mensagem na tela com o resultado da função
    print(opcao2(c_ou_s) + ler(nome))
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()