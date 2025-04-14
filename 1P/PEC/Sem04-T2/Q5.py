#Armazenando dados em uma variável
nota1 = int(input('Para calcular a média ponderada de três alunos digite aqui o primeiro número:'))
nota2 = int(input('Agora digite aqui o segundo número:'))
nota3 = int(input('E aqui o terceiro número:'))
#Calculando as notas
nota1 = nota1*2
nota2 = nota2*3
nota3 = nota3*5
nota = nota1+nota2+nota3
mediaponderada = nota/10
#Imprimindo resultado na tela do usuário
print('Média ponderada dos alunos:',mediaponderada)