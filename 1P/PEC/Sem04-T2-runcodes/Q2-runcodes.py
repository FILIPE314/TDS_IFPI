#Armazenando dados em uma variável
idade = int(input().strip())
#Armazenando dados em uma variável
mes = int(input().strip())
#Armazenando dados em uma variável
dia = int(input().strip())
#Calculando os dados
mes = 30*mes+dia
ano = 365*idade
dia = ano+mes
#Imprimindo o resultado na tela do usuário
print(dia)