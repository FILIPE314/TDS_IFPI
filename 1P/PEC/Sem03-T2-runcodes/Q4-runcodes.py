#Imprimindo conteúdo para o usuário com interação
mint = float(input().strip())
#Variantes para fazer cálculos
horas = mint/60
mintrest = mint%60
#Transformando numeros reais para inteiros
horas = int(horas)
mintrest = int(mintrest)
#Transformando nimeros inteiros para string
horas = str(horas)
mintrest = str(mintrest)
#Adicionando as letras que faltavam
result = horas+'h'+mintrest+'min'
#Imprimindo o resultado na tela do usuário
print(result)