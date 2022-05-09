#Author: William Monte de Moura
#Aula: 7

#Escreva um programa que pergunte a quantidade de quilômetro(s) percorrido(s) por um carro alugado e a quantidade de
#dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que a diária do carro custa R$60,00 por dia e R$0,15
#por quilômetro rodado.
print('Carro Alugado')

dal= int(input('Quantos dias foi alugado?'))
dalug = dal * 60  # Variável "dalug" é igual a dias de aluguel.
km = float(input('Quantos quilômetros foram rodados?'))
dist = km * 0.15  # Variável "dist" é igual a distância percorrida pelo carro.

total = dalug + dist  # Variável "total" é igual ao valor a ser cobrado pelo carro.

print('O valor a ser cobra do pelo aluguel do carro, será: R${:.2f}'.format(total))