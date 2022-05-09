#Author: William Monte de Moura
#Aula: 7

#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média:
nta1 = float(input('Nota 01 = '))
nta2 = float(input('Nota 02 = '))
snta = nta1 + nta2
print('A soma das notas 01 e 02 é: {}'.format(snta))
mnta = snta / 2
print("A média das notas 01 e 02 é: {:.2f}".format(mnta))