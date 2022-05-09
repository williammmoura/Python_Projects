#Author: William Monte de Moura
#Aula: 14

#   Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

#from math import factorial

n = int(input('Digite um número, inteiro e não-negativo, para o cálculo de seu fatorial (n!):'))

#Contador:
c = n
nfat = 1 #Para iniciar a multiplicação.

print('Calculando {}! = '.format(n), end='')
#calculo de n!:
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')  #if dentro do print.
    nfat = nfat * c
    c -= 1
print('{}'.format(nfat))