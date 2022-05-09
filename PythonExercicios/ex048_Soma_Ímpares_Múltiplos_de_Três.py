#Author: William Monte de Moura
#Aula: 13

#   Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo
#de 1 até 500.

#Criando acumulador:
soma = 0

#Criando um contador:
cont = 0

#Fazendo o laço de repetição:
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1    #Estou contando os números divisiveis por 3.
        soma = soma + c    #Estou acumulando números os números divisivel por 3.
print('A soma de todos os {} valores solicitados é {}.'.format(cont, soma))