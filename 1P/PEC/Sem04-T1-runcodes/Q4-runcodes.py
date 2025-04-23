#Armazenando dados em uma variável e imprimindo uma mensagem para o usuário.
hora = int(input().strip())
minuto = int(input().strip())
segundo = int(input().strip())
#Fazendo os calcúlos.
hora = hora*60
minuto = minuto*60+segundo
segundo = hora*60+minuto
#Imprimindo a data formatada na ordem certa.
print(segundo)