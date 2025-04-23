#Imprimir a pergunta na tela do computador do usuário com interação
segundos = int(input('Para saber quantos minutos tem em quantos segundos você quiser, digite os segundos:').strip())
#Calcular quantos minutos tem dependendo do número de segundos
minutos = segundos//60
result1 = segundos%60
#Resultado de tudo
print('Essa quantidade de segndos tem', minutos,'minutos e ainda sobram', result1,'segundos')