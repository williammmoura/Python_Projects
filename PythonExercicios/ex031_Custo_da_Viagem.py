#Author: William Monte de Moura
#Aula: 10

#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
# Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input('Qual é a distância, em quilômetros, de sua viagem?'))
p1 = dist * 0.50
p2 = dist * 0.45
if dist <= 200:
    print('O preço da viagem será de R${:.2f}.'.format(p1))
else:
    print('O preço da viagem será de R${:.2f}.'.format(p2))