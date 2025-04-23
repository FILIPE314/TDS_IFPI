def main():
    while True:
        print('''OPÇÕES:
1 - SAUDAÇÃO
2 - BRONCA
3 - FELICITAÇÃO
0 - FIM''')
        opcao = int(input().strip())
        if opcao == 1:
            print('1 - Olá. Como vai?')
        elif opcao == 2:
            print('2 - Vamos estudar mais.')
        elif opcao == 3:
            print('3 - Meus Parabéns!')
        elif opcao == 0:
            print('0 - Fim de serviço.')
            break
        else:
            print('Opção inválida.')

if __name__ == '__main__':
    main()