# condicional(complementar) que verifica o resultado
def quiz1(resultado1):
    # condicional(complementar) que verifica a resposta do usuário
    if resultado1 == 'b':
        # retorna o resultado se essa for a opção
        return 'Tá sabendo ein. :)'
    # condicional(complementar) que verifica a resposta do usuário
    elif resultado1 == 'c':
        # retorna o resultado se essa for a opção
        return 'Não é essa não mano. :('
    # condicional(complementar) que verifica a resposta do usuário
    elif resultado1 == 'a':
        # retorna o resultado se essa for a opção
        return 'Não é essa não mano. :('
    # condicional(falsa ou contrária)
    else:
        # retorna o resultado se essa for a opção
        return 'Essa letra ai não ta nas opções não :('
# condicional(complementar) que verifica o resultado
def quiz2(resultado2):
    # condicional(complementar) que verifica a resposta do usuário
    if resultado2 == 'c':
        # retorna o resultado se essa for a opção
        return 'Tá sabendo ein. :)'
    # condicional(complementar) que verifica a resposta do usuário
    elif resultado2 == 'b':
        # retorna o resultado se essa for a opção
        return 'Não é essa não mano. :('
    # condicional(complementar) que verifica a resposta do usuário
    elif resultado2 == 'a':
        # retorna o resultado se essa for a opção
        return 'Não é essa não mano. :('
    # condicional(falsa ou contrária)
    else:
        # retorna o resultado se essa for a opção
        return 'Essa letra ai não ta nas opções não. :('
# condicional(complementar) que verifica o resultado
def quiz3(resultado3):
    # condicional(complementar) que verifica a resposta do usuário
    if resultado3 == 'a':
        # retorna o resultado se essa for a opção
        return 'Tá sabendo ein. :)'
    # condicional(complementar) que verifica a resposta do usuário
    elif resultado3 == 'b':
        # retorna o resultado se essa for a opção
        return 'Não é essa não mano. :('
    # condicional(complementar) que verifica a resposta do usuário
    elif resultado3 == 'c':
        # retorna o resultado se essa for a opção
        return 'Não é essa não mano. :('
    # condicional(falsa ou contrária)
    else:
        # retorna o resultado se essa for a opção
        return 'Essa letra ai não ta nas opções não. :('
# condicional(complementar) que verifica a resposta do usuário
def pont1(score,result1):
    # condicional(complementar) que verifica a resposta do usuário
    if result1 == 'Tá sabendo ein. :)':
        # retorna o resultado se essa for a opção
        return score + 1
    # condicional(falsa ou contrária)
    else:
        # retorna o resultado se essa for a opção
        return score + 0
# condicional(complementar) que verifica a resposta do usuário
def pont2(score,result2):
    # condicional(complementar) que verifica a resposta do usuário
    if result2 == 'Tá sabendo ein. :)':
        # retorna o resultado se essa for a opção
        return score + 1
    # condicional(falsa ou contrária)
    else:
        # retorna o resultado se essa for a opção
        return score + 0
# condicional(complementar) que verifica a resposta do usuário
def pont3(score,result3):
    # condicional(complementar) que verifica a resposta do usuário
    if result3 == 'Tá sabendo ein. :)':
        # retorna o resultado se essa for a opção
        return score + 1
    # condicional(falsa ou contrária)
    else:
        # retorna o resultado se essa for a opção
        return score + 0 
# função (main) que inicia e termina o programa
def main():
    # variável que guarda dados
    score = 0
    # imprime uma mensagem na tela
    print('1.Qual é o principal uso da função print() em Python?')
    # imprime uma mensagem na tela
    print('a) Ler entrada do usuário')
    # imprime uma mensagem na tela
    print('b) Exibir informações na tela')
    # imprime uma mensagem na tela
    print('c) Definir variáveis')
    # variável que armazena dados da entrada do usuário
    resultado1 = input('Digite só a letra:').lower()
    # imprime o resultado na tela usando a função
    print(quiz1(resultado1))
    # imprime uma mensagem na tela
    print('2.Qual é o operador usado para exponenciação em Python?')
    # imprime uma mensagem na tela
    print('a) ^')
    # imprime uma mensagem na tela
    print('b) //')
    # imprime uma mensagem na tela
    print('c) **')
    # variável que armazena dados da entrada do usuário
    resultado2 = input('Digite só a letra:').lower()
    # imprime o resultado na tela usando a função
    print(quiz2(resultado2))
    # imprime uma mensagem na tela
    print('3.Como se declara um comentário em Python?')
    # imprime uma mensagem na tela
    print('a) # Este é um comentário')
    # imprime uma mensagem na tela
    print('b) // Este é um comentário')
    # imprime uma mensagem na tela
    print('c) /* Este é um comentário */')
    # variável que armazena dados da entrada do usuário
    resultado3 = input('Digite só a letra:').lower()
    # imprime o resultado na tela usando a função
    print(quiz3(resultado3))
    # variável que armazena dados
    result1 = quiz1(resultado1)
    # variável que armazena dados
    result2 = quiz2(resultado2)
    # variável que armazena dados
    result3 = quiz3(resultado3)
    # variável que armazena dados
    pont11 = pont1(score,result1)
    # variável que armazena dados
    pont21 = pont2(score,result2)
    # variável que armazena dados
    pont31 = pont3(score,result3)
    # imprime uma mensagem na tela
    print(pont11+pont21+pont31,'essa é sua pontuação.')
    # imprime uma mensagem na tela
    print('Fim.Obrigado por jogar!')
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()