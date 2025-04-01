#Imprimindo conteúdo para o usuário com interação
produto = float(input('Para saber o preço de qualquer produto com 10''%'' de desconto digite aqui o preço do seu produto:'))
#Variantes para fazer cálculos
desconto = produto*90/100
#Imprimindo o resultado na tela do usuário
print(f'O valor do produto com o desconto é:{desconto:.2f}')