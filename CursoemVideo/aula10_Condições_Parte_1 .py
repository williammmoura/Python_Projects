########################################################################################################################
#############################################   CONDIÇÕES (PARTE 1)   ##################################################
########################################################################################################################

# A ideia dessa aula é criar opções para o programador. Anteriormente tinhamos uma sequencia definida, para chegar no
#objetivo do programa, agora poderemos ter duas (ou mais) condições para que o programa execute e chegue ao objetivo.

# Em resumo, dentro de um programa temos dois caminhos diferentes para chegar em um objetivo.


########################################################################################################################
##################################################   EXEMPLO   #########################################################

#                                      +++++++ carro.siga() +++++++
#                                      +                          +
#                                      +                          +
#                                 SE carro.esquerda()           SENÃO
#                                 carro.siga()               carro.siga()
#                                 carro.direita()            carro.esquerda()
#                                 carro.siga()               carro.siga()
#                                 carro.direita()            carro.esquerda()
#                                 carro.esquerda()           carro.siga()
#                                 carro.siga()                    +
#                                 carro.direita()                 +
#                                 carro.siga()                    +
#                                      +                          +
#                                      +                          +
#                                      ++++++++ carro.pare() ++++++

# Na programação ficará:

# carro.siga()
# SE carro.esquerda()
#   carro.siga()
#   carro.direita()
#   carro.siga()
#   carro.direita()
#   carro.esquerda()
#   carro.siga()
#   carro.direita()
#   carro.siga()
# SENÃO
#   carro.siga()
#   carro.esquerda()
#   carro.siga()
#   carro.esquerda()
#   carro.siga()
# carro.para()

# Analogamente:
# OBS.: Aqui não é a sintaxe do Python.

# SE carro.esquerda()
#    bloco_V_
# SENÃO
#    bloco_F_

#bloco_V_ (Verdadeiro)
#bloco_F_ (Falço)

#######################################   Usando a sintaxe do Pyton:   #################################################

#if carro.esquerda():  #NÃO ESQUECER DOS "DOIS PONTOS" (:) no final.
#    bloco True
#else:
#    bloco False

########################################################################################################################


########################################################################################################################
#####################################################   EXEMPLO 2   ####################################################

tempo = int(input('Quantos anos tem seu carro?'))
if tempo<=3:
    print('Carro novo.')
else:
    print('Carro velho.')
print('--FIM--')
print('=' * 55)

########################################################################################################################

########################################################################################################################
################################################   Condição Simplificada   #############################################

#tempo = int(input('Quantos anos tem seu carro?'))
#print('Carro novo'if <=3 else'Carro velho')
#print('--FIM--')

########################################################################################################################
########################################################################################################################

########################################################################################################################
######################################################   PRÁTICA   #####################################################
########################################################################################################################


########################################################################################################################
####################################################   Programa 01   ###################################################

nome = str(input('Qual é o seu nome?')).split()
if nome == 'William':
    print('Que nome lindo!')
else:
    print('Legal.')
print('Bom dia, {}!'.format(nome))

print('=' * 55)
########################################################################################################################


########################################################################################################################
####################################################   Programa 02   ###################################################

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
n3 = float(input('Digite a terceira nota:'))
m = (n1 + n2 + n3) / 3

print('A sua média foi: {:.2f}'.format(m))
if m >= 7.00:
    print('Sua média foi {:.2f}, logo você está aprovado. Parabéns'.format(m))
else:
    print('Sua média foi {:.2f}. Você terá que realizar o exame final. Bons Estudos.'.format(m))