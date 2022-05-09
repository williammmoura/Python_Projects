#Author: William Monte de Moura
#Aula: 8

#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mos
#tre o comprimento da hipotenusa.


'''caop = float(input('Comprimento do cateto oposto:'))
caad = float(input('Comprimento di cateto adjacente:'))
hip = (caop ** 2 + caad ** 2) ** (1/2)
print('Fazendo {}² + {}², temos o valor do comprimento da hipotenusa, que é: {:.2f}'.format(caop, caad, hip))'''


######################################   Fazendo de uma maneira mais "fácil"   #########################################

from math import hypot
caop = float(input('Comprimento do cateto oposto:'))
caad = float(input('Comprimento do cateto adjacente:'))
print('Fazendo {}² + {}², temos o valor do comprimento da hipotenusa, que é: {:.2f}'.format(caop, caad, hypot(caop,
                                                                                                              caad)))
