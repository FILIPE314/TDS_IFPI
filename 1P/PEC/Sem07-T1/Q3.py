# função condicional(composta) que retorna um resultado dependendo da resposta do ususário
def sinal(caractere):
    # condicional(complementar verdadeira) que verifica o resultado
    if caractere.upper() == 'V':
        # retorna o resutado caso seja esssa opção
        return 'Siga'
    # condicional(complementar verdadeira) que verifica o resultado
    elif caractere.upper() == 'A':
        # retorna o resutado caso seja esssa opção
        return 'Atenção'
    # condicional(complementar verdadeira) que verifica o resultado
    elif caractere.upper() == 'E':
        # retorna o resutado caso seja esssa opção
        return 'Pare'
    # condicional(falsa ou contrária)
    else:
        # retorna o resutado caso seja esssa opção
        return ' '
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    caractere = input('Digite aqui uma letra, para saber oque significa a cores do semáforo, a letra (V) significa verde, a letra (A) amarelo e a letra (E) vermelho:')
    # imprime uma mensagem na tela com o resultado da função
    print('Essa cor quer dizer:',sinal(caractere))
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()