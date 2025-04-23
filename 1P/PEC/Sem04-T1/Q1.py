#Armazenando dados em uma variável e imprimindo uma mensagem para o usuário
ano = int(input("Coloque aqui um ano de sua preferência:"))
#Armazenando dados em uma variável e imprimindo uma mensagem para o usuário
mes = int(input("Coloque aqui um mês de sua preferência:"))
#Armazenando dados em uma variável e imprimindo uma mensagem para o usuário
dia = int(input("Coloque aqui um dia de sua preferência:"))
#Transformando inteiros para string
ano = str(ano)
mes = str(mes)
dia = str(dia)
#Imprimindo a data formatada na ordem certa
print('Data:'+dia+'/'+mes+'/'+ano)