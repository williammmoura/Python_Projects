#Author: William Monte de Moura
#Aula: 13

#   Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
#digitado for ímpar, desconsidere-o.

#Criando acumulador:
soma = 0
#Criando contador:
cont = 0

print('*' * 60)
for q in range(1, 7):
    w = int(input('Digite o {}º número inteiro:'.format(q)))
    if w % 2 == 0:
        soma = soma + w
        cont = cont + 1
print('Considenrando apenas os número PARES, a soma deles foi: {}'.format(soma))
print('*' * 60)