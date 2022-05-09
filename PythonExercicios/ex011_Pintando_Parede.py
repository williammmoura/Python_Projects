#Author: William Monte de Moura
#Aula: 7

#Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta neces-
#sária para pinta-lá sabendo que cada litro de tinta, pinta uma área de 2m².
larg = float(input('Digite a largura da parede (em metros):'))
alt = float(input('Digite a altura da parede (em metros):'))
area = larg * alt
ltinta = area / 2
print('Sua parede tem dimensão {}X{} e a sua área é de {:.3}m².'.format(larg, alt, area))
print('Para pintar esta parede, você utilizará {:.3}L de tinta'.format(ltinta))