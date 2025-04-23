# função(condicional) que imprime um resultado
def calc_idade(ano,ano2):
    x = ano2 - ano
    return x
# função que define a idade da pessoa
def anos(dia,mes,dia2,mes2,idade):
    if dia == dia2 and mes == mes2:
        return idade
    elif dia > dia2 and mes > mes2:
        return idade - 1
    elif dia < dia2 and mes < mes2:
        return idade
    elif dia >= dia2 and mes < mes2:
        return idade - 1
    elif dia > dia2 and mes <= mes2:
        return idade - 1
    elif dia <= dia2 and mes > mes2:
        return idade
    elif dia < dia2 and mes >= mes2:
        return idade
    else:
        return idade
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    dia2 = int(input())
    # variável que imprime uma informação na tela e armazena dados
    mes2 = int(input())
    # variável que imprime uma informação na tela e armazena dados
    ano2 = int(input())
    # variável que imprime uma informação na tela e armazena dados
    dia = int(input())
    # variável que imprime uma informação na tela e armazena dados
    mes = int(input())
    # variável que imprime uma informação na tela e armazena dados
    ano = int(input())
    # variável armazena dados
    idade = calc_idade(ano,ano2)
    # imprime uma informação na tela
    print(anos(dia,mes,dia2,mes2,idade))
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()