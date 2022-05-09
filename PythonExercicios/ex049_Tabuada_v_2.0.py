#Author: William Monte de Moura
#Aula: 13

#   Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um número inteiro para ver a sua tabuada:'))
print('=' * 13)
for c in range(0, 11):
    x = n * c
    print('\033[36m{}\033[m * {:2} = \033[1;33m{}\033[m'.format(n, c, x))
print('=' * 13)