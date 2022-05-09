#Author: William Monte de Moura
#Aula: 7

#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada:

num = int(input('Digite um número:'))
dob = num * 2
tri = num * 3
raq = num ** (1/2)
print('O dobro do {} é:{};'.format(num, dob))
print('O triplo do {} é:{};'.format(num, tri))
print('A raiz quadrada do {} é:{}'.format(num, raq))
