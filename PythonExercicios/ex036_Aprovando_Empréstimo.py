#Author: William Monte de Moura
#Aula: 12

#   Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salá-
# rio do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o em-
# préstimo será negado.

valorcasa = float(input('Qual é o valor do imóvel? R$'))
sro = float(input('Qual é a sua renda mensal? R$'))
tempo = int(input('Quantos anos de financiamento?'))

#30% do salário:
sro30 = sro * 30 / 100
#Calculo da prestação:
prest = valorcasa / (tempo * 12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}.'.format(valorcasa, tempo, prest))
#Condições:
if prest <= sro30:
    print('O emprestimo pode ser CONCEDIDO.')
else:
    print('Empréstimo NEGADO!')
