#Author: William Monte de Moura
#Aula: 10

#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.



print('=-' * 70)
print('Analisador de Triângulos')
print('=-' * 70)
print('Colocando os valores dos segmentos de reta:')
sr1 = float(input('Primeiro segmento de reta:'))
sr2 = float(input('Segundo segmento de reta:'))
sr3 = float(input('Terceiro segmento de reta:'))

from time import sleep
from termcolor import colored
print(colored('PROCESSANDO...', 'yellow'))
sleep(3)

if sr1 < sr2 + sr3 and sr2 < sr1 + sr3 and sr3 < sr1 + sr2:
    print('Os segmentos de retas acima PODEM formar um triângulo.')
else:
    print('Os segmentos de retas acima NÃO PODEM formar um triângulo ')