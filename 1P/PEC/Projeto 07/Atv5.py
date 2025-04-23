alfabeto = 'abcdefghijklmnopqrstuvwxyz'

mensagem = input('Por favor, entre com mensagem a ser criptografada: ').lower()
mensagemCriptografada = ''
chave = int(input('Digite a sua chave: '))

for char in mensagem:
    if char in alfabeto:
        posicao = alfabeto.find(char)
        novaPosicao = (posicao + chave) % 26
        mensagemCriptografada += alfabeto[novaPosicao]
    else:   
        mensagemCriptografada += char

print(f'Sua menssagem criptografada é: {mensagemCriptografada}')   