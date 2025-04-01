#Imprimir a pergunta na tela do computador do usuário com interação
distância = float(input().strip())
nave = float(input().strip())
#Calcular quantas dia e quantas horas levará para chegar ao destino
horas = distância/nave
dias = horas/24
dias2 = horas%24
#Transformnado para números inteiros
horas = int(horas)
dias = int(dias)
dias2 = int(dias2)
#Resultado de tudo
print(dias,'dias e', dias2, 'horas')