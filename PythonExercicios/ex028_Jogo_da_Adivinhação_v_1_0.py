#Author: William Monte de Moura
#Aula: 10


# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar desco-
#brir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
from termcolor import colored

computador = randint(1, 6)    #Faz o computador "pensar".

print(colored('-*-','blue') * 25)
print('   ' * 25)
print('Tente advinhar, entre 1 a 6, qual é o número que eu estou pensando.')
print('   ' * 25)
print(colored('-*-','blue') * 25)

jogador = int(input('E aí, já sabe o número, de 1 a 6, que eu pensei? Digite ao lado:'))# O jogador tenta advinhar o nú-
#mero.

print(colored('PROCESSANDO...','yellow'))
sleep(3)

if jogador == computador:
    print((colored('Parabéns! Eu pensei extamente no número {}!','green',)
                        .format(computador)))
else:
    print(colored('Você errou! Eu pensei no número {}.','red').format(computador))