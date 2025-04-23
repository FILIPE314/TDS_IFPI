# função(condicional) que imprime um resultado
def calc_idade(ano,ano2):
    x = ano2 - ano
    return x
# função que define a idade da pessoa
def anos(dia,mes,dia2,mes2,idade):
    if dia == dia2 and mes == mes2:
        return idade
    elif dia >= dia2 and mes >= mes2:
        return idade - 1
    elif dia <= dia2 and mes <= mes2:
        return idade + 1
    elif dia >= dia2 and mes <= mes2:
        return idade + 1
    elif dia <= dia2 and mes >= mes2:
        return idade - 1
    else:
        return idade - 1
# função (main) que inicia e termina o programa
def main():
    # imprime uma informação na tela
    print('Digite a data de  hoje e depois a data do seu nascimento, para sua idade ser calculada')
    # variável que imprime uma informação na tela e armazena dados
    dia2 = int(input('Coloque aqui o dia de hoje:'))
    # variável que imprime uma informação na tela e armazena dados
    mes2 = int(input('Coloque aqui o mês:'))
    # variável que imprime uma informação na tela e armazena dados
    ano2 = int(input('Coloque aqui o ano: '))
    # variável que imprime uma informação na tela e armazena dados
    dia = int(input('Coloque aqui o dia do seu nascimento:'))
    # variável que imprime uma informação na tela e armazena dados
    mes = int(input('Coloque aqui o mês de seu nascimento:'))
    # variável que imprime uma informação na tela e armazena dados
    ano = int(input('Coloque aqui o ano de seu nascimento:'))
    # variável armazena dados
    idade = calc_idade(ano,ano2)
    # imprime uma informação na tela
    print('Sua idade é:',anos(dia,mes,dia2,mes2,idade),' anos')
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()