#Imprimir a pergunta na tela do computador do usuário com interação
print('Digamos que você vai fazer poções mágicas, na loja só há 3 ingredientes escolha a quantidade desejada dos itens e vamos calcular o quanto você gastou')
iten1 = int(input('Pó de Lua Estelar:').strip())
iten2 = int(input('Essência de Dragão:').strip())
iten3 = int(input('Lágrimas de Fênix:').strip())
#Calcular a quantidade de itens que a pessoa quer com o valor de cada iten
preçoiten1 = iten1*5
preçoiten2 = iten2*3
preçoiten3 = iten3*8
#Resultado de tudo
print('Total a pagar:', preçoiten1+preçoiten2+preçoiten3)