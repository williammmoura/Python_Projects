########################################################################################################################
###########################################   Estrutura de repetição for   #############################################
########################################################################################################################

###################################################    TEORIA   ########################################################

#   Os "laços" de repetições (iteração), facilitam na compactação do programa, ou seja, se tiver que fazer vários passos
#para chegar em um objetivo, com o laço (neste caso usaremos o "for") diminuo a quantidade de COMANDOS para chegar no
#objetivo final.

#Exemplo ilustrativo (1):

#   LaçoCnoIntervalo(1,10):   "C" -> Variável de controle (pode colocar qualquer nome).
#       passo      O comando "passo" está na indentação. Para colocar outros comandos, tenho que colocar na mesma indentação.
#   pega           O comando "pega" está fora do laço de repetição.

#Exemplo com sintaxe PYTHON (1):

#   forCinrange(1,10):   Não esquecer do ":".
#       passo
#   pega

#Exemplo ilustrativo (2):

#   LaçoCnoIntervalo(1,3):
#       passo
#       pula
#   passo
#   pega

#Exemplo com sintaxe PYTHON (2):

#   forCinrange(1,3):   Não esquecer do ":".
#       passo
#       pula
#   passo
#   pega

#Exemplo ilustrativo (3):

#   LaçoCnoIntervalo(1,3):
#       se moeda:    Aqui temos, dentro do laço, uma condicional.
#            pega    ***NOTE A ESTRUTURA!***
#       passo
#       pula
#   passo
#   pega

#Exemplo com sintaxe PYTHON (3):

#   forCinrange(1,3):   Não esquecer do ":".
#       if moeda:
#           pega
#       passo
#       pula
#   passo
#   pega

########################################################################################################################
##################################################   PRÁTICA   #########################################################
########################################################################################################################

#Sem o laço de repetição:
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')

print('=' * 3)

#Com o laço de repetição:
for c in range (0, 6):  #Começa a contar a partir do ZERO!
    print('Oi')
print('FIM')

print('=' * 3)

for c in range (0, 6):
    print('Oi')
    print('FIM')   #Mudando a tabulação.

print('=' * 3)

for c in range (0, 6):
    print(c)       #Irá fazer de 0 a 5
print('FIM')

print('=' * 3)

for c in range (6, 0):  #Não irá contar de 6 até 0.
    print(c)
print('FIM')

print('=' * 3)

for c in range (6, 0, -1):  #Colocando o -1 irá contar de 6 até 0.
    print(c)
print('FIM')

print('=' * 3)

for c in range (0, 7, 2):  #O ultimo termo dará a iteração. No caso, contará de 2 em 2
    print(c)
print('FIM')

print('=' * 3)

n = int(input('Digite um número:'))
for v in range(0, n):
    print(v)
print('Fim!')
#Repare que não chegou até o número digitado.

print('=' * 3)

n = int(input('Digite um número:'))
for v in range(0, n + 1):
    print(v)
print('Fim!')
#Agora sim, irá até o numero digitado.

print('=' * 3)

i = int(input('Início:'))
f = int(input('Fim:'))
p = int(input('Passo:'))
for b in range(i, f + 1, p):
    print(b)
print('Fim!')

print('=' * 3)

for w in range(0, 3):
    r = int(input('Digite um valor'))  #Vai pedir o valor 3x.
print('Fim!')

print('=' * 3)

s = 0
for q in range(0, 4):
    r = int(input('Digite um valor'))  #Vai pedir o valor 3x.
    s += q
print('A soma de todos os valores foi: {}'.format(s))