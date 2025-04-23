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
    # variável que imprime uma informação na tela e armazena dados
    dia2 = input().strip()
    # variável que imprime uma informação na tela e armazena dados
    mes2 = input().strip()
    # variável que imprime uma informação na tela e armazena dados
    ano2 = input().strip()
    # variável que imprime uma informação na tela e armazena dados
    dia = input().strip()
    # variável que imprime uma informação na tela e armazena dados
    mes = input().strip()
    # variável que imprime uma informação na tela e armazena dados
    ano = input().strip()
    # aciona a função
    recente(dia,mes,dia2,mes2,ano,ano2)
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()