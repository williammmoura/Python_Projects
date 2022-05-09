#Author: William Monte de Moura
#Aula: 7

#Escreva um programa que leia um valor em metros e p exiba convertido em centímetros e milímetros:
n = float(input('Coloque um valor de medida em metros:'))
print('A coversão de medida é fornecida abaixo:')
cent = n * 100
print('{} metro(s), equivale(m) a {} centímetro(s).'.format(n, cent))
mil = n * 1000
print('{} metro(s), equivale(m) a {} milímetro(s).'.format(n, mil))

print(''*1)

########################################################################################################################
####################################################   Extra   #########################################################
########################################################################################################################
print('Extra')

print(''*1)
dm = n * 10
print('{} metro(s), equivale(m) a {} decímetro(s).'.format(n, dm))
dam = n / 10
print('{} metro(s), equivale(m) a {} decametro(s).'.format(n, dam))
hm = n / 100
print('{} metro(s), equivale(m) a {} hectometro(s).'.format(n, hm))
km = n / 1000
print('{} metro(s), equivale(m) a {} quilômetro(s).'.format(n, km))