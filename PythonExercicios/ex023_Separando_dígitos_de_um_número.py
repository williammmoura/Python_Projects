#Author: William Monte de Moura
#Aula: 9

#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados:
#Exemplo:
#Digite o número: 1834
#Unidade: 4;
#Dezena: 3;
#Centena: 8;
#Milhar: 1.
num = int(input('Digite um número:'))
u = num // 1 % 10    ####   Aqui, foi feito a DIVISÃO INTEIRA (//) e depois o MÓDULO (%)
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

######  OBS.: É importante (% 10), isso significa que eu irei tirar apenas uma unidade.
from time import sleep
print('Analisando o número {}...'.format(num))
sleep(3)
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))