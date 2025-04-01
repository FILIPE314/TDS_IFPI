# =============================================================================================================================================================
# Questão 15
def calculate(num):
    if num > 0:
        result = 0
        for i in range(1, num + 1):
            result += (i ** 2 + 1) / (i + 3)
        return f'O resultado de um calculo muito doido: {result}'
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
# =============================================================================================================================================================