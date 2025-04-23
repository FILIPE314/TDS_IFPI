# descriptogravar omqemd = caesar

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

chave = int(input('Digite a sua chave: ')) 
# chave = -chave ou (posicao - chave) % 26

letra = input('Por favor, entre com letra para descriptografar: ')
posicao= alfabeto.find(letra)

novaPosicao = (posicao - chave) % 26

letraDESCriptografada = alfabeto[novaPosicao]
print(f'Sua letra descriptografar é: {letraDESCriptografada}')