#Author: William Monte de Moura
#Aula: Aula 4

#2) Faça um programa que leia o nome de uma pessoa e dê a mensagem de boas-vindas.

nome = input('Digite seu nome:')
print('Bem-vindo,',nome,'!')
idade = input('Qual é a sua idade?')
print('Obrigado(a) pelas informações.')

#Com saida formatada:
print('É um prazer em te conhecer, {}!'.format(nome))

#O nome será colocado entre chaves, no resultado final.