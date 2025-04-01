#Imprimir a pergunta na tela do computador do usuário com interação
fatias = int(input().strip())
#Mesma coisa de cima só que agora com a quantidade de amigos
amigos = int(input().strip())
#Calcular quantas fatias para cada amigo e quatas sobrarão
result1 = fatias//amigos
result2 = fatias%amigos
print(result1)
print(result2)