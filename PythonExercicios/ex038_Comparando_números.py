#Author: William Monte de Moura
#Aula: 12

#   Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais
#Titulo com perfumaria:
print('\033[1;36m-*\033[m' * 20)
print('\033[1;30;46mComparando Números\033[m')
print('\033[1;36m-*\033[m' * 20)
#Valores de entrada, fornecidas pelo o usuário:
num1 = int(input('Digite um número inteiro qualquer:'))
num2 = int(input('Digite um número inteiro qualquer:'))
#Condições:
if num1 > num2:
    print('O primeiro número é maior.')
elif num2 > num1:
    print('O segundo número é maior.')
else:
    print('Os dois números são iguais.')