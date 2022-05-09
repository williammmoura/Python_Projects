#Author: William Monte de Moura
#Aula: 13

#   Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
#com uma pausa de 1 segundo entre eles.

print('Contagem Regressiva')

from time import sleep
from emoji import emojize

for c in range (10, -1, -1):     #Foi colocado -1, no segundo range, para que a contgem chegue até 0.
    sleep(1)
    print(c)
print(emojize(':fireworks: :fireworks: Feliz Ano Novo!:fireworks: :fireworks:'))