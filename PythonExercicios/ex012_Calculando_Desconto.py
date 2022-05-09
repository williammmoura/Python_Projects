#Author: William Monte de Moura
#Aula: 7

#Faça um algoritmo que leia o preço do produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Digite o preço do produto (em reais): R$'))
preço5 = preço - ((preço * 5) / 100)
print('Com o desconto de 5% no valor de R${:.2f}, o novo valor será de R${:.2f}.'.format(preço, preço5))