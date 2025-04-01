#Armazenando dados em uma variável e imprimindo uma mensagem para o usuário
altura = float(input().strip())
#Armazenando dados em uma variável e imprimindo uma mensagem para o usuário.
comprimento = float(input().strip())
#Armazenando dados em uma variável e imprimindo uma mensagem para o usuário.
largura = float(input().strip())
#Calculando a área do piso.
areadopiso = comprimento*largura
#Calculando o volume do cômodo.
volume = altura*comprimento*largura
#Calculando a área da parede.
areadaparede = 2*comprimento*altura+2*largura*altura
#Transformando para números inteiros.
areadopiso = int(areadopiso)
areadaparede = int(areadaparede)
volume = int(volume)
#Imprimindo o resultado na tela.
print(f'{areadopiso}')
print(f'{volume}')
print(f'{areadaparede}')