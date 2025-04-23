# função que calcula o IMC
def calc_imc(peso,altura):
    imc = peso/(altura*altura)
    return imc
# função que verifica o resultado do IMC
def verifica_resultado(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc >= 18.5 and imc < 25:
        return 'Peso normal'
    elif imc >= 25 and imc < 30:
        return 'Sobrepeso'
    elif imc >= 30 and imc < 35:
        return 'Obeso leve'
    elif imc >= 35 and imc < 40:
        return 'Obeso moderado'
    elif imc >= 40:
        return 'Obeso mórbido'
# função (main) que inicia e termina o programa
def main():
    # variável que imprime uma informação na tela e armazena dados
    peso = float(input('Digite seu peso para saber o seu IMC:'))
    # variável que imprime uma informação na tela e armazena dados
    altura = float(input('Digite sua altura para saber o seu IMC:'))
    # calculando o IMC
    imc = calc_imc(peso,altura)
    # verificando o resultado do IMC
    resultado = verifica_resultado(imc)
    # Imprimindo o resultado na tela do computador do usuário
    print(f'{resultado:.2f}')
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()