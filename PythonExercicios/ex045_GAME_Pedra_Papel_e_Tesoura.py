#Author: William Monte de Moura
#Aula: 12

#   Crie um programa que faça o computador jogar Jokenpô com você.

#Importando randint da biblioteca random:
from random import randint
from emoji import emojize


#Perfuaria:
print('=' * 53)
print('{:^23}'.format('                    \033[1;30;41mJ\033[1;30;43mo\033[1;30;42mk\033[1;30;44me\033[1;30;45mn\033[1;'
                      '30;46mp\033[1;30;47mô\033[1;31;40m!\033[m'))
print('=' * 53)
print('''   Jokenpô, também chamado de Pedra, Papel e Tesoura,
é um jogo de mãos recreativo e simples para duas ou
mais pessoas. Aqui você irá jogar comigo...o talen-
toso WillNote! ;)
            \033[1;36;43m*Regras*\033[m
\033[1;33;46mPedra ganha da tesoura (amassando-a ou quebrando-a).\033[m
\033[1;33;46mTesoura ganha do papel (cortando-o).\033[m
\033[1;33;46mPapel ganha da pedra (embrulhando-a).\033[m''')
print('=' * 53)

#Usando "while" para fazer o loop.
#Variável "r" para criar opção de resposta.
r = 'S'
while r == 'S':    #Aqui a condição para continuar o jogo é o "S".

    # Criando uma lista (0,1,2)
    itens = ('PEDRA', 'PAPEL', 'TESOURA')

    # O computador irá buscar na lista, de forma aleatória.
    # Ou seja, aqui será a "JOGADA DO PC".
    pc = randint(0, 2)

    #Mostrando as opções para o usuário:
    print('Confira as opções abaixo:')
    print('''[ 0 ] -> PEDRA;
[ 1 ] -> PAPEL;
[ 2 ] -> TESOURA.''')

    #Jogada do usuário
    player = int(input('Digite o número da opção correspondente:'))

    #Perfumaria:
    from time import sleep
    print('\033[1;30;41mJ\033[1;30;43mO\033[m')
    sleep(0.5)
    print('  \033[1;30;42mK\033[1;30;44mE\033[1;30;45mN\033[m')
    sleep(0.5)
    print('     \033[1;30;46mP\033[1;30;47mO\033[1;31;40m!!!\033[m')
    print('=' * 53)

    #Mostrando o resultado das jogadas do PC e Usuário:
    print('WillNote jogou {}.'.format(itens[pc]))
    print('Você jogou {}.'.format(itens[player]))
    print('=' * 53)

    #Condições para vencedor:
    if pc == 0:   #pc jogou PEDRA:
        if player == 0:
            print('\033[1;30;47mEMPATE!\033[m')
        elif player == 1:
            print(emojize('\033[0;30;44mVocê GANHOU!\033[m :sunglasses:'))
        elif player == 2:
            print('\033[0;30;41mWillNote GANHOU!\033[m')
        else:
            print('Jogada \033[0;41mINVÁLIDA!\033[m Tente novamente.')
    elif pc == 1: #pc jogou PAPEL:
        if player == 0:
            print('\033[0;30;41mWillNote GANHOU!\033[m')
        elif player == 1:
            print('\033[1;30;47mEMPATE!\033[m')
        elif player == 2:
            print(emojize('\033[0;30;44mVocê GANHOU!\033[m :sunglasses:'))
        else:
            print('Jogada \033[0;41mINVÁLIDA!\033[m Tente novamente.')
    elif pc == 2:  #pc jogou TESOURA.
        if player == 0:
            print(emojize('\033[0;30;44mVocê GANHOU!\033[m :sunglasses:'))
        elif player == 1:
            print('\033[0;30;41mWillNote GANHOU!\033[m')
        elif player == 2:
            print('\033[1;30;47mEMPATE!\033[m')
        else:
            print('Jogada \033[0;41mINVÁLIDA!\033[m Tente novamente.')
        print('=' * 53)
    r = str(input('Deseja jogar novamente? [S/N] ')).upper()
    print('=' * 53)
print('')