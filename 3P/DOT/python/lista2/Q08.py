# 8) Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes 
# ocorreu a letra ‘A’. OBS: Fazer crítica na entrada do caractere para aceitar somente letras.
def verifica_letra(lista):
    repetido = 0
    for i in range(len(lista)):
        if 'a' == lista[i]:
            repetido += 1
    return f'\nA letra (A) apareceu {repetido} vezes nessa lista\n'
def main():
    lista = []
    while True:
        try:
            for i in range(10):
                letra = input('\nDigite uma letra para compor uma lista e depois ver quantas vezes a letra (A) apareceu: ').lower()
                if letra.isalpha() and len(letra) == 1:
                    lista.append(letra)
                else:
                    print('\nDigite um valor válido, nesse caso letras\n')
                    continue
            print(verifica_letra(lista))
            break
        except ValueError:
            print(f'\nOps... Algo de errado não está certo, digite um valor válido!')
if __name__ == '__main__':
    main()