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

def populacaoMaior(populacao, cidades):
    maiores = []
    for cidadeInfo in cidades:
        if cidadeInfo[5] > populacao:
            maiores.append(f'IBGE: {cidadeInfo[1]} - {cidadeInfo[2]}({cidadeInfo[0]}) - POPULAÇÃO: {cidadeInfo[5]}')

    print(f'CIDADES COM MAIS DE {populacao} HABITANTES:')
    for i in maiores:
        print(i)

def main():
    populacao = int(input('População: ').strip())
    cidades = carrega_cidades()

    populacaoMaior(populacao, cidades)

if __name__ == '__main__':
    main()