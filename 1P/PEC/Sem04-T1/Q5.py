#Armazenando dados em uma variável e imprimindo uma mensagem para o usuário
altura = float(input('Se você está reformando sua casa e quer saber a área do piso, a área das paredes e o volume do cômodo, digite aqui a altura do cômodo:'))
#Armazenando dados em uma variável e imprimindo uma mensagem para o usuário
comprimento = float(input('Agora o comprimento do cômodo:'))
#Armazenando dados em uma variável e imprimindo uma mensagem para o usuário
largura = float(input('A largura do cômodo:'))
#Calculando a área do piso
areadopiso = comprimento*largura
#Calculando o volume do cômodo
volume = altura*comprimento*largura
#Calculando a área da parede
areadaparede = 2*comprimento*altura+2*largura*altura
#Transformando para números inteiros
areadopiso = int(areadopiso)
areadaparede = int(areadaparede)
volume = int(volume)
#Imprimindo o resultado na tela
print('Área do piso:',areadopiso)
print('Volume do cômodo:',volume)
print('Área da parede:',areadaparede)