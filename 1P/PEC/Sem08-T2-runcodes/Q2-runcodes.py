# Função que calcula a soma dos dígitos do número.
def soma_digitos(numero):
    soma = 0
    for digito in str(numero):
        if digito.isdigit():
            soma += int(digito)
    return soma
# Verifica se o número está entre 0 e 100.000
def soma_digitos2(numero,num):
    if 0 < numero < 100000:
        # Calcula a soma dos dígitos usando a função soma_digitos
        resultado = num
        # Retorna o resultado
        print(resultado)
    else:
        # Caso contrário, imprime -1
        print("-1")
# função (main) que inicia e termina o programa
def main():
    # Variável que imprime uma informação na tela e armazena dados
    numero = int(input().strip())
    # Variável que imprime uma informação na tela e armazena dados
    num = soma_digitos(numero)
    # Aciona a função
    soma_digitos2(numero,num)
# Complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()