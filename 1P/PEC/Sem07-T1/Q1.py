# função condicional que retorna um resultado dependendo da resposta do ususário
def sexo(masculino_ou_feminino):
    # condicional(verdadeira) que verifica o resultado
    if masculino_ou_feminino == '1':
        # retorna o resutado caso seja esssa opção
        return 'Ilmo Sr.'
    # condicional(falsa ou contrária)
    else:
        # retorna o resutado caso seja esssa opção
        return 'Ilma Sra.'
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    nome = input('Digite aqui seu nome:')
    # variável que imprime uma informação na tela e armazena dados
    masculino_ou_feminino = input('Agora digite 1 se seu sexo for masculino e digite 2 caso seja feminino:')
    # imprime uma mensagem na tela com o resultado da função
    print('Seu sexo é', sexo(masculino_ou_feminino),'e seu nome é', nome)
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()