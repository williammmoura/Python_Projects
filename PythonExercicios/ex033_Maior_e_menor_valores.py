#Author: William Monte de Moura
#Aula: 10

#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

valor1 = float(input('Digite um número qualquer:'))
valor2 = float(input('Digite um número qualquer:'))
valor3 = float(input('Digite um número qualquer:'))

#Verificando quem é o menor.
menor = valor1
if valor2 < valor1 and valor2 < valor3:
    menor = valor2
if valor3 < valor1 and valor3 < valor2:
    menor = valor3

#Verificando quem é o maior.
maior = valor1
if valor2 > valor1 and valor2 > valor3:
    maior = valor2
if valor3 >  valor1 and valor3 > valor2:
    maior = valor3

print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))
