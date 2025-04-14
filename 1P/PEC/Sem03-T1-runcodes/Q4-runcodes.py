#Imprimir a pergunta na tela do computador do usuário com interação
segundos = int(input().strip())
#Calcular quantos minutos tem dependendo do número de segundos
minutos = segundos//60
result1 = segundos%60
#Resultado de tudo
print(minutos)
print(result1)