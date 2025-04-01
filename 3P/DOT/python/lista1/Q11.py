# =============================================================================================================================================================
# Questão 11
def divisores(num):
    if 0 < num:
        som = 0
        for i in range(1, num + 1):
            if num % i == 0:
                som += 1
        return f'O número {num} tem {som} divisores'
    else:
        return 'Ops... Valor inválido!'
def main():
    while True:
        try:
            num = int(input('Digite um numero e saiba quantos divisores esse número tem: '))
            print(divisores(num))
            break
        except:
            print('Ops... Valor inválido!')
if __name__ == '__main__':
    main()