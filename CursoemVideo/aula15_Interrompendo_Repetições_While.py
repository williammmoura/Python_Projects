########################################################################################################################
##########################################   Interrompendo repetições while   ##########################################
########################################################################################################################

###################################################    TEORIA   ########################################################

#   Nessa aula, vamos aprender como utilizar a instrução break e os loopings infinitos a favor das nossas estratégias de
#código. É muito importante saber usar o break no Python, já que em alguns casos precisamos interromper um laço no meio
#do caminho.

# Além disso, vamos aprender como trabalhar com as novas fstrings do Python.


#   Exemplo ilustrativo (1):
# enquanto VERDADEIRO:
#    se chão:
#      passo
#    se buraco:
#      pula
#    se moeda:
#      paga
#    se troféu:
#      pula
#      para      #Neste momento o programa para o loop, pois foi achado o troféu ("resultado final") e pega o objeto.
# pega

#    Na sintaxe Python:
# while True:
#    if chão:
#      passo
#    if buraco:
#      pula
#    if moeda:
#      pega
#    if troféu:
#      pula
#      break       #Neste momento o programa para o loop, pois foi achado o troféu ("resultado final") e pega o objeto.
# pega


########################################################################################################################
#######################################################   PRÁTICA   ####################################################
########################################################################################################################

#Contador
cont = 0
while cont <= 10:   #Aqui estou delimitando quantas vezes o programa efetuará o loop (no caso, até 10).
    print(cont,'->', end='')
    cont += 1
print('Acabou!')


#Loop infinito.
#while True


#Usando FLAG
#n = 0
#while n != 999:  #O 999 será o FLAG, ou seja, delimitará o final do programa.
#    n = int(input('Digite um número:'))


#Para "quebra" (break) o loop (sem usar o flag).
n = s = 0
while True:   #Loop infinito
    n = int(input('Digite um número:'))
    if n == 999:
        break
    s += n
#print('A soma vale {}.'.format(s))

# Usando "fstring".
print(f'A soma vale {s}.')

##########################################    Mais exemplos com "fstrings"   ###########################################

nome =  'José'
idade = 33
print(f'O {nome} tem {idade} anos.') #PYTHON 3.6+