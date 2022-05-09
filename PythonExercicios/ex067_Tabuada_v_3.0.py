#Author: William Monte de Moura
#Aula: 15

#   Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O
#programa será interrompido quando o número solicitado for negativo.

while True:
    n = int(input('Digite um número inteiro para verificar a sua tabuada:'))
    print('Para finalizar o programa digite um número negativo.')
    if n < 0:
        break
    print('-' * 30)
    for c in range (0 , 11):
        print(f'\033[36m{n}\033[m x {c} = \033[1;33m{n*c}\033[m')
    print('-' * 30)
print('FIM.')