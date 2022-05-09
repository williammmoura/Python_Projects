#Author: William Monte de Moura
#Aula: 14

#   Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usa-
#ndo a estrutura while.

print('Dez termos de uma Progressão Aritmética (PA)')

#Variáveis:
t = int(input('Digite o primeiro termo da PA:'))
r = int(input('Digite a razão da PA:'))

#Contador:
termo = t
cont = 1

while cont <= 10:
    print('{} → '.format(termo), end='')
    termo = termo + r
    cont += 1
print('FIM.')