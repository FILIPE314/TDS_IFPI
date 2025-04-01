# =============================================================================================================================================================
# Questão 13
def calculate(num):
    if num > 0:
        result = 0
        for i in range(1, num + 1):
            result += (1 / i)
        return f'Resultado de uma soma maluca: {result}'
    else:
        return 'Ops... Valor inválido!'
def main():
    while True:
        try:
            num = int(input('Digite um número para fazer uma soma muito doida: '))
            print(calculate(num))
            break
        except:
            print('Ops... Valor inválido!')
if __name__ == '__main__':
    main()