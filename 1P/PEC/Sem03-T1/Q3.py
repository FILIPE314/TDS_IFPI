#Imprimir a pergunta na tela do computador do usuário com interação
doces = int(input('Para embalar uma certa quantidade de doces digite a quantidade de doces que você quer embalar:'))
caixas = int(input('Agora digite o número de caixas que você deseja usar para embalar os doces:'))
#Calcular quantos vão em cada caixa
result = doces/caixas
result = int(result)
#Resultado de tudo
print('Haverá', result,'doces para cada', caixas,'caixa(s)')