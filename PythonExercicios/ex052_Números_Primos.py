#Author: William Monte de Moura
#Aula: 13

#   Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

#O número primo só pode ser divisível 2 vezes. Ou seja, divisível por 1 ou por ele mesmo.

print('Vamos verificar se o número digitado é um número primo.')
n = int(input('Digite um número:'))

#Contador
tot = 0  #Para saber quantos números de divisíveis.

for c in range (1, n + 1):
    #Para destacar quais números são divisíveis e quais não são reespectivamente.
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1   #IGUAL -> tot = tot + 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(n, tot))   #\n -> Quebra de linha
## end= é para não pular linha! ##
if tot == 2:
    print('E por isso, {} É PRIMO!'.format(n))
else:
    print('E por isso, {} NÃO É PRIMO.'.format(n))