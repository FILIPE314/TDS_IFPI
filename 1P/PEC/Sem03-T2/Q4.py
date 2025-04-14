#Imprimindo conteúdo para o usuário com interação
mint = float(input('Programa que transforma minutos, em horas e miutos respectivamente, digite aqui quantos minutos você quer transformar:'))
#Transformando minutos para número inteiro
mint = int(mint)
#Variantes para fazer cálculos
horas = mint/60
mintrest = mint%60
#Transformando numeros reais para inteiros
horas = int(horas)
mintrest = int(mintrest)
#Imprimindo o resultado na tela do usuário
print('A quantidade de minutos colocada dão exatamente:', horas,'horas e', mintrest,'minutos')