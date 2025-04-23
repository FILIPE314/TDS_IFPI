# inicializa as contagens de números pares e ímpares
pares = 0
impares = 0
# lê os 100 números inteiros positivos
for numero in range(100):
    numero = int(input(f'Digite o {numero+1}º número inteiro positivo: '))
    # verifica se o número é positivo
    if numero > 0:
        # verifica se o número é par ou ímpar e atualiza as contagens
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    else:
        print("Por favor, digite um número inteiro positivo.")
# função (main) que inicia e termina o programa
def main():
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()