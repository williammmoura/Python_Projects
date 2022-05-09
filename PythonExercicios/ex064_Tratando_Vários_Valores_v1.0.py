#Author: William Monte de Moura
#Aula: 14

#   Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
#valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
#(desconsiderando o flag).

print('Digite qualquer número inteiro. O programa irá pedir diversas vezes, para o usuário digitar um número.')
print('A condição de parada será o número 999.')
#Contador.
n = 0  #Número inicial.
cont = 0  #Contador para ler a quantidade de números fornecidos pelo o usuário.
soma = 0
#n = cont = soma = 0
n = int(input('Digite um número inteiro (digitar 999 encera o progama):'))
while n != 999:  #Condição de parada.
    soma += n
    cont += 1
    n = int(input('Digite um número inteiro (digitar 999 encera o progama):'))
print('Você digitou {} números e a soma entre eles (não considera o 999) é {}.'.format(cont, soma))


# Tive repetir o comando de entrado (n), antes do "while" e no final do mesmo para tirar o flag (999).