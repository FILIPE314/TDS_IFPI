# =============================================================================================================================================================
# Questão 9
def interval(num1, num2):
    if num1 >= 0 and num2 >= 0:
        soma = 0
        for i in range(num1 + 1, num2):
            soma += i
        return f'Resultao da soma entre o intervalo: {soma}'
    else:
        return f'Ops... Valor inválido!'
def main():
    while True:
        try:
            print('Digite dois número para saber a soma do intervalo entre eles')
            num1 = int(input('Digite o primeiro número: '))
            num2 = int(input('Digite o segundo número: '))
            if num1 < num2:
                print(interval(num1, num2))
                break
            else:
                print('Ops... Valor inválido!')
        except:
            print('Ops... Valor inválido!')
if __name__ == '__main__':
    main()