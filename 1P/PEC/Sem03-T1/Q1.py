#Imprimir a pergunta na tela do computador do usuário com interação
fatias = int(input('Digamos que você comprou uma pizza e vai dividir ela para seus amigos, para saber quantas fatias ficarão para cada um deles e quantas fatias vão sobrar digite o numero de fatias:'))
#Mesma coisa de cima só que agora com a quantidade de amigos
amigos = int(input('Agora digite quantos amigos vão comer a pizza:'))
#Calcular quantas fatias para cada amigo e quatas sobrarão
result1 = fatias//amigos
result2 = fatias%amigos
print("Cada um ficara com", result1," fatias de pizza e sobrarão", result2," fatias de pizza")