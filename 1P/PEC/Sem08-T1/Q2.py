# função que define qual data é mais recente
def recente(dia,mes,dia2,mes2,ano,ano2):
    if dia == dia2 and mes == mes2 and ano == ano2:
        print(dia+'/'+mes+'/'+ano)
    elif dia >= dia2 and mes >= mes2 and ano >= ano2:
        print(dia+'/'+mes+'/'+ano)
    elif dia <= dia2 and mes <= mes2 and ano <= ano2:
        print(dia2+'/'+mes2+'/'+ano2)
    elif dia >= dia2 and mes <= mes2 and ano <= ano2:
        print(dia2+'/'+mes2+'/'+ano2)
    elif dia <= dia2 and mes >= mes2 and ano >= ano2:
        print(dia+'/'+mes+'/'+ano)
    elif dia >= dia2 and mes >= mes2 and ano <= ano2:
        print(dia2+'/'+mes2+'/'+ano2)
    elif dia <= dia2 and mes <= mes2 and ano >= ano2:
        print(dia+'/'+mes+'/'+ano)
    else:
        print(dia+'/'+mes+'/'+ano)
# função (main) que inicia e termina o programa
def main():
    # imprime uma informação na tela
    print('Digite duas datas para ser calculado qual das duas é a mais recente')
    # variável que imprime uma informação na tela e armazena dados
    dia2 = int(input('Digite aqui o dia:'))
    # variável que imprime uma informação na tela e armazena dados
    mes2 = int(input('Digite aqui o mês:'))
    # variável que imprime uma informação na tela e armazena dados
    ano2 = int(input('Digite aqui o ano:'))
    # variável que imprime uma informação na tela e armazena dados
    dia = int(input('Digite aqui o dia:'))
    # variável que imprime uma informação na tela e armazena dados
    mes = int(input('Digite aqui o mês:'))
    # variável que imprime uma informação na tela e armazena dados
    ano = int(input('Digite aqui o ano:'))
    # aciona a função
    recente(dia,mes,dia2,mes2,ano,ano2)
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()