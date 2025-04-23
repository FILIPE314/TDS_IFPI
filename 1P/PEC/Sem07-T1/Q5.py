# função condicional(composta) que retorna um resultado dependendo da resposta do ususário
def cond(nota1,nota2,nota3):
    # condicional(complementar) que verifica o resultado
    if 8 < nota3 <= 10:
        # retorna o resutado caso seja esssa opção
        return (nota1 + nota2 + nota3) / 3 + 1
    # condicional(complementar) que verifica o resultado
    elif 8 < nota3 >= 10:
        # retorna o resutado caso seja esssa opção
        return (nota1 + nota2 + nota3) / 3 + 1
    # condicional(falsa ou contrária)
    else:
        # retorna o resutado caso seja esssa opção
        return (nota1 + nota2 + nota3) / 3
# função condicional(composta) que retorna um resultado dependendo da resposta do ususário
def media(func):
    # condicional(complementar) que verifica o resultado
    if func > 10:
        # retorna o resutado caso seja esssa opção
        return 10
    # condicional(falsa ou contrária)
    else:
        # retorna o resutado caso seja esssa opção
        return func
# função (main) que inicia e termina o programa
def main():
    # imprime uma informação na tela
    print('Para saber a média entre 3 notas, coloque as notas aa seguir.')
    # variável que imprime uma informação na tela e armazena dados
    nota1 = float(input('Nota 1:'))
    # variável que imprime uma informação na tela e armazena dados
    nota2 = float(input('Nota 2:'))
    # variável que imprime uma informação na tela e armazena dados
    nota3 = float(input('Nota 3:'))
    # variável que armazena dados calculados por uma função
    func = cond(nota1,nota2,nota3)
    # imprime uma mensagem na tela com o resultado da função
    print('Essa é a sua média:',media(func))
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()