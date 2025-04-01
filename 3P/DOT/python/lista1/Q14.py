# =============================================================================================================================================================
# Questão 14
def calculate(num):
    if num > 0:
        factorial = 1
        calc2 = 1
        for i in range(1, num + 1):
            factorial *= i
            calc2 += 1 / factorial
        return f'O calc2ado de um calculo muito doido: {calc2}'
    else:
        return 'Ops... Valor inválido, tente novamente'
def main():
    while True:
        try:
            num = int(input('Digite um número para fazer um cáculo muito louco: '))
            print(calculate(num))
            break
        except:
            print('Ops... Valor inválido, tente novamente')
if __name__ == '__main__':
    main()