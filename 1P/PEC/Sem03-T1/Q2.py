#Imprimir a pergunta na tela do computador do usuário com interação
distância = float(input('Para descobrir quantos dias e horas você leva ate chegar em um planeta coloque a distância do planeta em quilômetros:'))
nave = float(input('Agora coloque aqui a velocidade da nave em quilômetros por hora:'))
#Calcular quantas dia e quantas horas levará para chegar ao destino
horas = distância/nave
dias = nave/horas
#Transformnado para números inteiros
horas = int(horas)
dias = int(dias)
#Resultado de tudo
print('Você levará', horas,'horas e', dias,'dias para chegar até o planeta desejado.')