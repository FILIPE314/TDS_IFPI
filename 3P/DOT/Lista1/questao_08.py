# 8. Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'. Se o
# caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'. Use esta função em um
# programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. O programa deve ficar lendo os
# números até o usuário responder 'N' à pergunta se ele deseja continuar ou não.

def ler_escolha():
    while True:
        caractere = input("\nDigite um caractere ('S' ou 'N'): ").upper()
        if caractere == "S":
            return "S"
        elif caractere == "N":
            return 'N'
        else:
            print("\nERRO: Caractere inválido, digite novamente!")
    
def main():
    while True:
        try:
            num = float(input("\nDigite um número: "))
            print(f"\nO cubo de {num} é: {num**3}")
            
            escolha = ler_escolha()
            if escolha == "N":
                break
            else:
                continue
        except:
            print("\nERRO: Entrada inválida, digite apenas números!")
if __name__=="__main__":
    main()
