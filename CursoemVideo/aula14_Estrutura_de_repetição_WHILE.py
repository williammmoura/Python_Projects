########################################################################################################################
#####################################   Estrutura de repetição while (Enquanto)   ######################################
########################################################################################################################

###################################################    TEORIA   ########################################################

#   Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a estrutura de repetição while no Python.

#Por exemplo:

#c=1
#while c != 10:
#print(c)
#c+=1
#print(‘Acabou’)


########################################################################################################################
####################################################   IMPORTANTE!   ###################################################
########################################################################################################################

#   No "while"(Enquanto) não preciso colocar, um limite, para a quantidade de vezes que irá repetir um comando.

########################################################################################################################

#   Exemplo ilustrativo (1):
# enquanto não maçã:
#    passo
# pega

#   Na sintaxe Python:
# while not maçã:
#    passo
# pega

# Note, que while = enquanto.

#   Exemplo ilustrativo (2):
# enquanto não maçã:
#    se chão:
#    passo
#    se buraco:
#    pula
#    se moeda:
#    paga
# pega

#    Na sintaxe Python:
# while not maçã:
#    if chão:
#    passo
#    if buraco:
#    pula
#    if moeda:
#    pega
# pega


########################################################################################################################
#######################################################   PRÁTICA   ####################################################
########################################################################################################################

# Usando for:
for c in range(1, 10):
    print(c)
print('Fim.')

print('=' * 10)

# Usando while:
c = 1   #contador começando com 1.
while c < 10:   #"Enquanto o contador(c) for menor do que 10:"
    print(c)
    c += 1      #Aqui, assim que, o loop é feito, Ele adiconará mais 1.
print('Fim.')

print('=' * 10)

#for:
for c in range (1, 5):
    n = int(input('Digite um valor:'))
print('Fim.')

print('=' * 10)

#while:
n = 1
while n != 0:   #Condição de parada  # != -> Diferente
    n = int(input('Digite um valor:'))
print('Fim.')

print('=' * 10)

#   Usar no jogo JOKENPÔ!
r = 'S'
while r == 'S':
    n = int(input('Digite um valor:'))
    r = str(input('Quer continuar? [S/N]')).upper()
print('Fim.')

print('=' * 10)

#While (com gambiara)
n = 1
par = impar = 0
while n != 0:  # A condição para continuar o loop é digitando números diferentes(!=) de zero!
    n = int(input('Digite um valor:'))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))

print('=' * 10)