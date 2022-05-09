#Author: William Monte de Moura
#Aula: 9

#Crie um programa que leia o nome de uma pessoa e mostre:
#Nome com todas as letras em maiúsculas e minúsculas;
#Quantas letras possui (sem considerar os espaços);
#Quanta letras tem o primeiro nome.

from time import sleep
nome = str(input('Digite o seu nome completo:')).strip() # ".strip" elimina os espaços no inicio e no final.
print('Analisando seu nome...')
sleep(3)
print('Seu nome, em letras maiúsculas, é: {}'.format(nome.upper()))
print('Seu nome, em letras minúsculas, é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' '))) #Aqui temos a quantidade de letras, com os
#espaços ("len"), menos o contador de espaços ("count").
#print('Seu primeiro possui {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))