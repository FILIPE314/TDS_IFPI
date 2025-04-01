# =============================================================================================================================================================
# Questão 12
def somatorio(num):
    if num > 0:
        result = 0
        for i in range(1, num + 1):
            result += i
        return f'O somatório do número digitado é: {result}'
    else:
        return 'Ops... Valor inválido!'
def main():
    while True:
        try:
            num = int(input('Digite um número para saber seu somatório: '))
            print(somatorio(num))
            break
        except:
            print('Ops... Valor inválido!')
if __name__ == '__main__':
    main()