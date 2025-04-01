# função que calcula qual a média final
def med_f(num1,num2,num3,media):
    return (num1 + (num2 * 2) + (num3 * 3) + media) / 7
# função que verifica se a média final está alta ou baixa
def result1(media_final):
    if media_final >= 9:
        return 'A'
    elif 9 > media_final >= 7.5:
        return 'B'
    elif 7.5 > media_final >= 6:
        return 'C'
    elif 6 > media_final >= 4:
        return 'D'
    elif 4 > media_final:
        return 'E'
# função que imprime uma mensagem dependendo do valor atribuído da função anterior 
def media_final2(result):
    if result in 'ABC':
        return 'Aprovado'
    elif result in 'DE':
        return 'Reprovado'
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    matricula = input()
    # variável que imprime uma informação na tela e armazena dados
    num1 = float(input().strip())
    # variável que imprime uma informação na tela e armazena dados
    num2 = float(input().strip())
    # variável que imprime uma informação na tela e armazena dados
    num3 = float(input().strip())
    # variável que imprime uma informação na tela e armazena dados
    media = float(input().strip())
    # variável que armazena dados
    media_final = med_f(num1,num2,num3,media)
    # variável armazena dados
    result = result1(media_final)
    # imprime oque tem na variável
    print(matricula)
    # imprime o resultado da função
    print(f'{media_final:.2f}')
    # imprime oque tem na variável
    print(result)
    # aciona a função
    print(media_final2(result))
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()