# função que calcula e imprime um resultado
def ler(nome):
    # imprime uma mensagem na tela quando a função é acionada
    return len(nome)
# função condicional que retorna um resultado dependendo da resposta do ususário
def opcao2(c_ou_s):
    # condicional(complementar) que verifica o resultado
    if c_ou_s == '1':
        # variável local que contém uma entrada para o usuário dependendo da sua escolha
        nome_c = input('Coloque o nome do seu cônjugue:')
        ler2 = len(nome_c)
        # retorna o resutado caso seja esssa opção
        return ler2
    # condicional(falsa ou contrária)
    else:
        # retorna o resutado caso seja esssa opção
        return 0
# função (main) que inicia e termina o programa
def main():
    # imprime uma mensagem na tela
    print('Digite seu nome e seu estado civil, e se for casado o nome de seu cônjugue para saber quantas letras tem seu nome com o nome do seu cônjugue caso seja casado.')
    # variável que imprime uma informação na tela e armazena dados
    nome = input('Digite aqui seu nome:')
    # variável que imprime uma informação na tela e armazena dados
    c_ou_s = input('Agora digite 1 caso seja casado(a), se não digite 2 caso seja solteiro(a):')
    # imprime uma mensagem na tela com o resultado da função
    print(opcao2(c_ou_s) + ler(nome))
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()