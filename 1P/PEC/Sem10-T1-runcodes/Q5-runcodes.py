# variável que inicializa a variável para armazenar o maior número
maior_numero = 0
# lê os 100 números inteiros
for numero in range(100):
    numero = int(input().strip())
    # verifica se o número é positivo
    if numero > 0:
        # verifica se o número é maior que o maior número encontrado até agora
        if numero > maior_numero:
            maior_numero = numero
# função (main) que inicia e termina o programa
def main():
    print(f"{maior_numero}")
# complementar da função (main) essa encerra o programa
if __name__=='__main__':
    main()