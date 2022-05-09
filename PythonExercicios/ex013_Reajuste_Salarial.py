#Author: William Monte de Moura
#Aula: 7

#Faça um algoritmo que leia o salário de um colabordor e mostre o seu novo valor, com reajuste de 15%.

sro = float(input('Salário do colaborador: R$'))
raj = sro + ((sro * 15) / 100)
print('Com o reajuste de 15%, a mais, no valor de R${:.2f}. O novo salário será de R${:.2f}'.format(sro, raj))