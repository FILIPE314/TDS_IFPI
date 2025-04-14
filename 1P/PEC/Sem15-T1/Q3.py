def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado

def mesesExtenso(mes):
    if mes == 1: return 'JANEIRO'
    if mes == 2: return 'FEVEREIRO'
    if mes == 3: return 'MARÇO'
    if mes == 4: return 'ABRIL'
    if mes == 5: return 'MAIO'
    if mes == 6: return 'JUNHO'
    if mes == 7: return 'JULHO'
    if mes == 8: return 'AGOSTO'
    if mes == 9: return 'SETEMBRO'
    if mes == 10: return 'OUTUBRO'
    if mes == 11: return 'NOVEMBRO'
    if mes == 12: return 'DEZEMBRO'
    return 'Mês inválido'

def aniversario(dia, mes, cidades):
    aniversariantes = []
    for cidadeInfo in cidades:
        if cidadeInfo[3] == dia and cidadeInfo[4] == mes:
            aniversariantes.append(f'{cidadeInfo[2]}({cidadeInfo[0]})')

    print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE {mesesExtenso(mes)}:')
    for i in aniversariantes:
        print(i)

def main():
    dia = int(input('Dia: ').strip())
    mes = int(input('Mes: ').strip())
    cidades = carrega_cidades()

    aniversario(dia, mes, cidades)

if __name__ == '__main__':
    main()