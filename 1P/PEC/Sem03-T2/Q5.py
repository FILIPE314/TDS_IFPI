#Imprimindo conteúdo para o usuário com interação
tempo = float(input('Bonificação dos funcionários por tempo de trabalho, digite quantos anos você trabalho na empresa:'))
qntbônus = float(input('Agora coloque a quantidade de bônus por ano:'))
#Variantes para fazer cálculos
bônus = tempo*qntbônus
#Imprimindo o resultado na tela do usuário
print(f'{bônus:.2f}')