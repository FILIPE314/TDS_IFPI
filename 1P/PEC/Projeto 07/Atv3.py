alfabeto = 'abcdefghijklmnopqrstuvwxyz'

chave = int(input('Digite a sua chave: ')) 

letra = input('Por favor, entre com uma letra para criptografar: ')
posicao= alfabeto.find(letra)

novaPosicao = (posicao + chave) % 26

letraCriptografada = alfabeto[novaPosicao]
print(f'Sua letra criptografada é: {letraCriptografada}')