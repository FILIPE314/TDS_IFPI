#Armazenando dados em uma variável
nota1 = float(input().strip())
nota2 = float(input().strip())
nota3 = float(input().strip())
#Calculando as notas
nota1 = nota1*2
nota2 = nota2*3
nota3 = nota3*5
nota = nota1+nota2+nota3
mediaponderada = nota/10
#Imprimindo resultado na tela do usuário
print(f'{mediaponderada:.2f}')