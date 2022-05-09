#Author: William Monte de Moura
#Aula: 10


#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

from termcolor import colored

num = int(input('Digite um número inteiro:'))
resultado = num % 2   #RESTO DA DIVISÃO. RESTO ZERO É PAR, RESTO UM É ÍMPAR.
if resultado == 0:
    print('O número {} é PAR.'.format(num))
else:
    print('O número {} é ÍMPAR.'.format(num))