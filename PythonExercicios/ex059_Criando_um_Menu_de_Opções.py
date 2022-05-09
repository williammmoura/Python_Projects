#Author: William Monte de Moura
#Aula: 14

#   Crie um programa que leia dois valores e mostre um menu na tela:
#
# [ 1 ] somar
#
# [ 2 ] multiplicar
#
# [ 3 ] maior
#
# [ 4 ] novos números
#
# [ 5 ] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

print('Escolha dois números para, depois, selecionar qual a operação você deseja realizar.')

from time import sleep

n1 = float(input('Digite um valor numérico:'))
n2 = float(input('Digite um valor nemérico:'))

#Contador:
opcao = 0

#Condição de parada.
while opcao != 5:

    print('-=' * 50)

    print('''[ 1 ] -> SOMAR
[ 2 ] -> MULTIPLICAR
[ 3 ] -> MAIOR
[ 4 ] -> NOVOS NÚMEROS
[ 5 ] -> SAIR DO PROGRAMA''')

    #Input de dados:
    opcao = int(input('Qual é a sua opção?'))

    #Condições:
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação entre {} e {} é {}.'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior número é {}.'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite um valor numérico:'))
        n2 = int(input('Digite um valor numérico:'))
    elif opcao == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção INVALIDA!')

print('-=' * 50)

print('Fim do programa.')

print('-=' * 50)