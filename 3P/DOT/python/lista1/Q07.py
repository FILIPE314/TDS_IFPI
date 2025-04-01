# =============================================================================================================================================================
# Questão 7
def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fatorial(num - 1)
def main():
    while True:
        try:
            num = int(input('Digite um número e saiba seu valor em fatorial: '))
            if num > 0:
                print(f'O fatorial do número que você digitou é: {fatorial(num)}')
                break
            else:
                print('Ops... Valor inválido!')
        except:
            print('Ops... Valor inválido!')
if __name__ == '__main__':
    main()