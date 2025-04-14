# função condicional(composta) que retorna um resultado dependendo da resposta do ususário
def digt(caractere):
    # condicional(complementar verdadeira) que verifica o resultado
    if caractere.upper() in 'AEIOU':
        # retorna o resutado caso seja esssa opção
        return 'Vogal'
    # condicional(complementar verdadeira) que verifica o resultado
    elif caractere.upper() in 'BCDFGHJKLMNPQRSTVWXYZ':
        # retorna o resutado caso seja esssa opção
        return 'Consoante'
    # condicional(complementar verdadeira) que verifica o resultado
    elif caractere in '1234567890':
        # retorna o resutado caso seja esssa opção
        return 'Número'
    # condicional(falsa ou contrária)
    else:
        # retorna o resutado caso seja esssa opção
        return 'Símbolo'
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    caractere = input('Digite aqui um caractere para saber de que classe ele é:')
    # imprime uma mensagem na tela com o resultado da função
    print('Seu caractre é:',digt(caractere))
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()