#Author: William Monte de Moura
#Aula: 7

#Faça um algoritmo que leia temperatura em ºC (grau(s) Celsius) e converta para Fahrenheit e Kelvin.

tc = float(input('Qual é a temperatura (em grau(s) Celsius):'))
tf = (1.8 * tc) + 32
print('A temperatura {:.1f}ºC, corresponde a {:.1f}ºF (Fahrenheit).'.format(tc, tf))
tk = tc + 273
print('A temperatura {:.1f}ºC, corresponde a {:.1f}K (Kelvin).'.format(tc, tk))
