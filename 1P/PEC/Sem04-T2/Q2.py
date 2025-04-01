#Armazenando dados em uma variável
idade = int(input('Para saber a sua idade em dias coloque aqui sua idade:'))
#Armazenando dados em uma variável
mes = int(input('Agora aqui o mês em que você nasceu:'))
#Armazenando dados em uma variável
dia = int(input('Agora aqui digite o dia em que nasceu:'))
#Calculando os dados
mes = mes*30+dia
ano = 365*idade
dia = ano+mes
#Imprimindo o resultado na tela do usuário
print('Você tem atualmente',dia,'dias de nascido')