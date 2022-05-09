#Author: William Monte de Moura
#Aula: 8

#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
#Ex.: Digite um número: 6.127
#     O número 6.127, tem a parte inteira 6.

'''from math import trunc
num = float(input('Digite qualquer número real:'))
print('O número {} tem a porção inteira é igual a: {}'.format(num, trunc(num)))'''

####################################   Pode ser feito de outra maneira   ###############################################

num = float(input('Digite um número:'))
print('O número {} tem a sua porção inteira é igual a: {}'.format(num, int(num)))
