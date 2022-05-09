#Author: William Monte de Moura
#Aula: 12

#   Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#
#– EQUILÁTERO: todos os lados iguais;
#
#– ISÓSCELES: dois lados iguais, um diferente;
#
#– ESCALENO: todos os lados diferentes.

print('=' * 70)
print('Analisando Triângulos')
print('=' * 70)
seg1 = float(input('Primeiro segmento de reta:'))
seg2 = float(input('Segundo segmento de reta:'))
seg3 = float(input('Tericeiro segmento de reta:'))

from time import sleep
from termcolor import colored

print(colored('PROCESSANDO...', 'yellow'))
sleep(2)

#Teste de formação do triângulo:
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos de retas acima PODEM formar um triângulo ', end='') #'end=''' Permite colocar o outro 'print' na
    #mesma linha.
    #Teste para ver o tipo de triângulo:
    if seg1 == seg2 == seg3:
        print('EQUILATERO!')
    elif seg1 != seg2 != seg3 != seg1: # '!=' -> SINAL DE DIFERENTE.
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Os segmentos de retas acima NÃO PODEM formar um triângulo.')