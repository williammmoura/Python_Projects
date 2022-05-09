#Author: William Monte de Moura
#Aula: 14

#   Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai
#tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint     #Importando o pacote que faz "escolhas aleatórias".
from time import sleep
from termcolor import colored

#Usando "while" para fazer o loop.
#Variável "r" para criar opção de resposta.
r = 'S'
while r == 'S':    #Aqui a condição para continuar o jogo é o "S".

    computador = randint(0, 10)   #Aqui o computador irá "escolher" um número de 1 a 10.

    print(colored('-*-','blue') * 25)
    print('   ' * 25)
    print('Tente advinhar, entre 0 a 10, qual é o número que eu estou pensando.')
    print('   ' * 25)
    print(colored('-*-','blue') * 25)

    #Criando uma variável para verificar se está certo ou errado, o palpite:
    acertou = False

    #Contador de palpites:
    palpite = 0

    #Condição de parada (WHILE):
    while not acertou:
        jogador = int(input('E aí! Já sabe o número, de 0 a 10, que eu pensei? Digite ao lado:'))  # O jogador tenta ad
        # vinhar o número.
        print(colored('PROCESSANDO...', 'yellow'))
        sleep(2)
        palpite += 1  #A soma do número de palpites realizados.

        if jogador == computador:
            acertou = True
            print((colored('Parabéns! Eu pensei extamente no número {}!', 'green', )
                       .format(computador)))
        else:
            if jogador < computador:
                print(colored('MAIOR! Tente novamente.', 'red'))
            elif jogador > computador:
                print(colored('MENOR! Tente novamente.', 'red'))

    print('Você jogou {} vezes para acertar o número que o computador pensou.'.format(palpite))
    r = str(input('Deseja jogar novamente? [S/N] ')).upper()
    print('=' * 53)
print('')