# =============================================================================================================================================================
# Questão 4
def aprova_ou_reprova(nota1, nota2):   
    media = (nota1 + nota2) / 2
    if media >= 6:
        return f'PARABÉNS! Você foi aprovado!'
    else:
        return f'NÃO DESISTA! Você não foi aprovado!'
def main():
    while True:
        print('Para saber a se você foi aprovado, digite sua primeira e segunda nota.')
        try:
            nota1 = float(input('Sua primeira nota:'))
            nota2 = float(input('Sua segunda nota:'))
            if 10 >= nota1 >= 0 and 10 >= nota2 >= 0:
                print(aprova_ou_reprova(nota1, nota2))
                break
            else:
                print('Ops... Coloque valores válidos!')
        except:
            print('Ops... Coloque valores válidos!')
if __name__ == '__main__':
    main()    