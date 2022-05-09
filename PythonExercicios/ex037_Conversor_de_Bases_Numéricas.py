#Author: William Monte de Moura
#Aula: 12

#   Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
#conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

from time import sleep

num = int(input('Digite um número inteiro qualquer:'))
print('Escolha qual será a base de conversão:')
print('[ 1 ] -> Binário;')
print('[ 2 ] -> Octal; ')
print('[ 3 ] -> Hexadecimal.')
conv = int(input('Digite o número correspondente a opção desejada:'))

print('\033[1;31;43mCalculando...\033[m')
sleep(2)

if conv < 1 or conv > 3:
    print('Digite apenas um dos números correspondentes a opção desejada. \033[1;30;41mReinicie o programa.\033[m')
elif conv == 1:

    #Foi adicionado "[2:], no final de cada formatação, para eliminar os dois primeiro caracter que será mostrado na te-
    #la. Ou seja, será contado, os caracteres, a partir do terceiro elemento.

    print('{} convertido para BINÁRIO é igual a: {}'.format(num, bin(num)[2:]))
elif conv == 2:
    print('{} convertido para OCTAL é igual a: {}'.format(num, oct(num)[2:]))
elif conv == 3:
    print('{} convertido para HEXADECIMAL é igual a: {}'.format(num, hex(num)[2:]))

#OBS.: 0b -> binário;
#      0o -> octal;
#      0x -> hexadecimal.