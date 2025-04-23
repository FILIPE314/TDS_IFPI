def main():
    populacaoInicial = int(input('Digite o número referente a população de aves no início do ano 1600: '))
    populacaoAtual = populacaoInicial
    ano = 1599

    # O programa encerra sua execução quanto a população total cai para menos de 10% da população original.
    # populacaoAtual < 0.1 * populacaoInicial (FALSE)
    # populacaoAtual >= 0.1 * populacaoInicial (TRUE)

    while populacaoAtual >= 0.1 * populacaoInicial:
        nascimento = 0.01 * populacaoAtual
        mortes = 0.06 * populacaoAtual

        populacaoAtual = populacaoAtual + nascimento - mortes
        ano += 1

        print(f'Ano = {ano}, Nascimento = {nascimento:.0f}, Mortes = {mortes:.0f}, População Atual = {populacaoAtual:.0f}')

if __name__ == '__main__':
    main()