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

def populacaoMaior(mes, populacao, cidades):
    maiores = []
    for cidadeInfo in cidades:
        if cidadeInfo[4] == mes and cidadeInfo[5] > populacao:
            maiores.append(f'{cidadeInfo[2]}({cidadeInfo[0]}) tem {cidadeInfo[5]} habitantes e faz aniversário em {cidadeInfo[3]} de {mesesExtenso(mes).lower()}.')

    print(f'CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM {mesesExtenso(mes)}:')
    for i in maiores:
        print(i)

def main():
    mes = int(input('Mês: ').strip())
    populacao = int(input('População: ').strip())
    cidades = carrega_cidades()

    populacaoMaior(mes, populacao, cidades)

if __name__ == '__main__':
    main()