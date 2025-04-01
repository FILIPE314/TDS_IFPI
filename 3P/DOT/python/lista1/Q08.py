# =============================================================================================================================================================
# Questão 8
def quadrado(num):
    if num > 0:
        return f'O número que você digitou ao cubo: {num ** 3}'
    else:
        return False
def main():
    num = int(input('Digite um número para saber o seu valor em cubo: '))
    print(quadrado(num))
    while True:
        try:
            continuar = input('Deseja continuar? Digite (S) ou (N): ')
            if continuar == 'S':
                return main()
            elif continuar == 'N':
                break
            else:
                return f'Caractere inválido. Digite novamente' + False
        except:
            print('Ops... Valor inválido!')
if __name__ == '__main__':
    main()