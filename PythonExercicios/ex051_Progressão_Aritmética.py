#Author: William Monte de Moura
#Aula: 13

#   Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
#progressão.

print('Dez termos de uma Progressão Aritmética (PA)')
t = int(input('Digite o primeiro termo da PA:'))
r = int(input('Digite a razão da PA:'))
dez = t + (10 - 1) * r
for pa in range(t, dez + r, r):  #NOTE! 'dez + r', adicionei a razão para chegar ao décimo termo.
    print('{} '.format(pa), end='-> ')
print('ACABOU.')