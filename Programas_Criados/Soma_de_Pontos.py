#Author: William Monte de Moura
#Sum of points


from time import sleep

#Contador de rodadas:
rodada = 0

#Contador referente ao menu:
opcao = 0

#Contador para soma das rodadas:
#sp = p1 , p2 , p3, p4, p5, p6

#Condição de parada.
while opcao != 2:

    print('-=' * 50)
    print('Escolhas a opção [ 1 ] para começar o jogo:')
    print('''[ 1 ] -> PRÓXIMA RODADA
[ 2 ] -> SAIR E SOMAR OS RESULTADOS''')

    #Input de dados:
    opcao = int(input('Qual é a sua opção?'))

    #Condições:
    if opcao == 1:
        rodada += 1

        # Dados fornecidos pelo o usuário:
        print('\033[1;30;47mRodada {}'.format(rodada))
        p1 = int(input('\033[1;30;42mPontos player1:\033[m'))
        p2 = int(input('\033[1;30;43mPontos player2:\033[m'))
        p3 = int(input('\033[1;30;44mPontos player3:\033[m'))
        p4 = int(input('\033[1;30;45mPontos player4:\033[m'))
        p5 = int(input('\033[1;30;46mPontos player5:\033[m'))
        p6 = int(input('\033[1;30;47mPontos player6:\033[m'))
    elif opcao == 2:

        # Perfumaria:
        print('\033[1;33m=\033[m' * 50)
        print('\033[1;33mCalculando os pontos...\033[m')
        print('\033[1;33m=\033[m' * 50)
        sleep(2)

        # Calculos dos pontos:
        sp1 = p1
        print('O score final é \033[1;30;42m(P1): {}\033[m'.format(sp1))
        sp2 = p2
        print('O score final é \033[1;30;43m(P2): {}\033[m'.format(sp2))
        sp3 = p3
        print('O score final é \033[1;30;44m(P3): {}\033[m'.format(sp3))
        sp4 = p4
        print('O score final é \033[1;30;45m(P4): {}\033[m'.format(sp4))
        sp5 = p5
        print('O score final é \033[1;30;46m(P5): {}\033[m'.format(sp5))
        sp6 = p6
        print('O score final é \033[1;30;47m(P5): {}\033[m'.format(sp6))

        # Médias:
        msp1 = sp1 / rodada
        msp2 = sp2 / rodada
        msp3 = sp3 / rodada
        msp4 = sp4 / rodada
        msp5 = sp5 / rodada
        msp6 = sp6 / rodada

        # Condições para vencer:
        if not (not (sp1 > sp2) or not (sp1 > sp3)) and sp1 > sp4 and sp1 > sp5 and sp1 > sp6:
            print('\033[1;30;42mO Player 1, com {} ponto(s), ganhou! PARABÉNS!\033[m'.format(sp1))
            print('\033[1;30;42mMédia = {}\033[m'.format(msp1))
        elif sp2 > sp1 and sp2 > sp3 and sp2 > sp4 and sp2 > sp5 and sp2 > sp6:
            print('\033[1;30;43mO Player 2, com {} ponto(s), ganhou! PARABÉNS!\033[m'.format(sp2))
            print('\033[1;30;43mMédia = {}\033[m'.format(msp2))
        elif sp3 > sp1 and sp3 > sp2 and sp3 > sp4 and sp3 > sp5 and sp3 > sp6:
            print('\033[1;30;44mO Player 3, com {} ponto(s), ganhou! PARABÉNS!\033[m'.format(sp3))
            print('\033[1;30;44mMédia = {}\033[m'.format(msp3))
        elif sp4 > sp1 and sp4 > sp2 and sp4 > sp3 and sp1 > sp5 and sp4 > sp6:
            print('\033[1;30;45mO Player 4, com {} ponto(s), ganhou! PARABÉNS!\033[m'.format(sp4))
            print('\033[1;30;45mMédia = {}\033[m'.format(msp4))
        elif sp5 > sp1 and sp5 > sp2 and sp5 > sp3 and sp5 > sp4 and sp5 > sp6:
            print('\033[1;30;46mO Player 5, com {} ponto(s), ganhou! PARABÉNS!\033[m'.format(sp5))
            print('\033[1;30;46mMédia = {}\033[m'.format(msp5))
        elif sp6 > sp1 and sp6 > sp2 and sp6 > sp3 and sp6 > sp4 and sp6 > sp5:
            print('\033[1;30;47mO Player 6, com {} ponto(s), ganhou! PARABÉNS!\033[m'.format(sp5))
            print('\033[1;30;47mMédia = {}\033[m'.format(msp6))
    else:
        print('Opção INVALIDA!')
print('-=' * 50)
