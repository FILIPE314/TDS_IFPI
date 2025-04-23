# função que verifica a resposta do usuário
def q1(pergunta1):
    if pergunta1.upper() == 'S':
        return 1
    else:
        return 0
# função que verifica a resposta do usuário
def q2(pergunta2):
    if pergunta2.upper() == 'S':
        return 1
    else:
        return 0
# função que verifica a resposta do usuário
def q3(pergunta3):
    if pergunta3.upper() == 'S':
        return 1
    else:
        return 0
# função que verifica a resposta do usuário
def q4(pergunta4):
    if pergunta4.upper() == 'S':
        return 1
    else:
        return 0
# função que verifica a resposta do usuário
def q5(pergunta5):
    if pergunta5.upper() == 'S':
        return 1
    else:
        return 0
# função que calcula o resultado final e imprime uma mensagem de acordo com o resultado
def result_final(resultado):
    if resultado == 2:
        return 'Suspeito'
    elif resultado == 3 or resultado == 4:
        return 'Cúmplice'
    elif resultado == 5:
        return 'Assassino'
    else:
        return 'Inocente'
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela
    print('Responda a algumas perguntas para a investigação, só respoda com (S) ou (N)')
    # variável que imprime uma informação na tela e armazena dados
    pergunta1 = input('Telefonou para a vítima ?')
    # variável que imprime uma informação na tela e armazena dados
    pergunta2 = input('Esteve no local do crime ?')
    # variável que imprime uma informação na tela e armazena dados
    pergunta3 = input('Mora perto da vítima ?')
    # variável que imprime uma informação na tela e armazena dados
    pergunta4 = input('Devia para a vítima ?')
    # variável que imprime uma informação na tela e armazena dados
    pergunta5 = input('Já trabalhou com a vítima ?')
    # variável que calcula e armazena dados
    resultado = q1(pergunta1) + q2(pergunta2) + q3(pergunta3) + q4(pergunta4) + q5(pergunta5)
    # acionando a função e imprimindo
    print(result_final(resultado))
# complementar da função (main) essa encerra o programa
if __name__ == '__main__':
    main()