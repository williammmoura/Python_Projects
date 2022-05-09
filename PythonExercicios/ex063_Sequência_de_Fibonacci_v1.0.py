#Author: William Monte de Moura
#Aula: 14

#   Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência
#de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

#   É uma sucessão de números que, misteriosamente, aparece em muitos fenômenos da natureza. Descrita no final do século
#12 pelo italiano Leonardo Fibonacci, ela é infinita e começa com 0 e 1. Os números seguintes são sempre a soma dos dois
#números anteriores. Portanto, depois de 0 e 1, vêm 1, 2, 3, 5, 8, 13, 21, 34…

print('=' * 65)
print('Sequência de Fibonacci')
print('=' * 65)

n = int(input('Quantos termos, da Sequência de Fibonacci, você quer mostrar?'))

#Definindo os dois primeiros termos da sequência (são sempre 0 e 1).
t1 = 0
t2 = 1
print('~' * 65)
#Mostrando os dois primeiros termos.
print('{} → {} →'.format(t1,t2), end='')
#Contador para mostrar o número desejado de termos, que o usuário quer ver (a partir do 3, já que os dois primeiros ter-
#mos são conhecidos).
cont = 3

#Condição (enquanto "cont" for menor/igual a "n").
while cont <= n:
    t3 = t1 + t2
    print(' {} →'.format(t3), end='')
    #Troca de valor dos termos para fazer a soma da Sequência de Fibonacci.
    t1 = t2
    t2 = t3
    cont += 1
print(' FIM.')
