#Author: William Monte de Moura
#Aula: 6


#Faça um programa que leia algo pelo techado e mostre na tela o seu tipo primitivo e todas as informações possíveis
#sobre ele:
n = (input('Digite algo:'))
print(''*1)
#1)Tipo primitivo:
print('1)O tipo primitivo desse valor é: {}'.format(type(n)))
print(''*1)
#2)Alpha-numérico:
print('2)É um alpha-numérico? {}'.format(n.isalnum()))
print(''*1)
#3)Letra:
print('3)É uma letra? {}'.format(n.isalpha()))
print(''*1)
#4)
print('4) {}'.format(n.isascii()))
print(''*1)
#5)Decimal:
print('5)É um decimal? {}'.format(n.isdecimal()))
print(''*1)
#6)
print('6) {}'.format(n.isascii()))
print(''*1)
#7)
print('7) {}'.format(n.isdigit()))
print(''*1)
#8)Letra minúscula:
print('8)É letra minúscula? {}'.format(n.islower()))
print(''*1)
#9)É impressa:
print('9)É impressa? {}'.format(n.isprintable()))
print(''*1)
#10)Espaço:
print('10)É um espaço? {}'.format(n.isspace()))
print(''*1)
#11)Está em maiúscula:
print('11)Está capitalizada (maiúscula e minúscula)? {}'.format(n.istitle()))
print(''*1)
#12)Letra maiúscula:
print('12)É letra maiúscula? {}'.format(n.isupper()))