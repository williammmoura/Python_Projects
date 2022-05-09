#Author: William Monte de Moura
#Aula: 8

#Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e tangente.

from math import sin, cos, tan, radians
ang = float(input('Digite um valor angular (em graus) qualquer:'))

################################################   IMPORTANTE!!!!   ####################################################
###################################   Temos que converter de radianos para graus   #####################################

sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

########################################################################################################################

print('O Seno de {}º é igual a {:.2f}'.format(ang, sen))
#OBS.: SENO = Comprimento vertical.
print('O Cosseno de {}º é igual a {:.2f}'. format(ang, cos))
#OBS.: COSSENO = Comprimento horizontal.
print('A tangente de {}º é igual a {:.2f}'.format(ang, tan))
#OBS.: TANGENTE = Comprimento até a reta, que tange o círculo trigonométrico.