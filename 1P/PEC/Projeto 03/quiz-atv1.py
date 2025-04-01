# condicional(complementar) que verifica o resultado
def quiz(resultado):
    # condicional(complementar) que verifica a resposta do usuário
    if resultado == 'b':
        # retorna o resultado se essa for a opção
        return 'Tá sabendo ein. :)'
    # condicional(falsa ou contrária)
    else:
        # retorna o resultado se essa for a opção
        return 'Não era essa não mano. :('
# função (main) que inicia e termina o programa
def main():
    # imprime uma mensagem na tela
    print('Qual dessas opções é o número PI?')
    # imprime uma mensagem na tela
    print('a) 12,5647')
    # imprime uma mensagem na tela
    print('b) 3.14')
    # imprime uma mensagem na tela
    print('c) 10')
    # variável que armazena dados da entrada do usuário
    resultado = input('Digite só a letra:').strip()
    # imprime o resultado na tela usando a função
    print(quiz(resultado))
    # imprime uma mensagem na tela
    print('Obrigado por jogar!')
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()