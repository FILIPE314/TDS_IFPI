# 3) Faça um programa que dada uma seqüência de n números, imprimi-la na ordem inversa à da 
# leitura.
def contrario(sequencia):
    sequencia_contraria = []
    for i in range(len(sequencia) - 1, - 1, - 1):
        sequencia_contraria.append(sequencia[i])
    return f'Sequência que você digitou ao contrário {sequencia_contraria}'
def main():
    sequencia = []
    while True:
        try:
            num = int(input('Digite um número para formar uma sequencia e mostra-los ao contrário: '))
            sequencia.append(num)
            continuar = input('Quer continuar?(s para SIM e n para NÃO)\n').upper()
            if continuar == 'N':
                break
            elif continuar == 'S':
                continue
            else:
                print(f'\nOps... Algo de errado não está certo, digite uma resposta válida!')
        except:
            print(f'\nOps... Algo de errado não está certo, digite um valor válido!')
    print(contrario(sequencia))
if __name__ == '__main__':
    main()