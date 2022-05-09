########################################################################################################################
###############################################   Condições Aninhadas   ################################################
########################################################################################################################

######################################################   TEORIA   ######################################################

#Estrutura condicional dentro de uma estrutura condicional = aninhar

#Exemplo:

#             se carro.esquerda()
#                carro.siga()
#                carro.direita()
#                carro.siga()
#                carro.direita()
#                carro.esquerda()
#                carro.siga()
#                carro.direira()
#                carro.siga()
#             senão se carro.direita()
#                carro.siga()
#                carro.esquerda()
#                carro.siga()
#                carro.esquerda()
#                carro.siga()
#             senão
#                carro.siga()
#             carro.para()

#Exemplo em Python:

#             carro.siga()
#             if carro.esquerda():    NÃO ESQUECER DOS DOIS PONTOS (:)
#                carro.siga()
#                carro.direita()
#                carro.siga()
#                carro.direita()
#                carro.esquerda()
#                carro.siga()
#                carro.direira()
#                carro.siga()
#             elif carro.direita():   NÃO ESQUECER DOS DOIS PONTOS (:)
#                carro.siga()
#                carro.esquerda()
#                carro.siga()
#                carro.esquerda()
#                carro.siga()
#             else:                   NÃO ESQUECER DOS DOIS PONTOS (:)
#                carro.siga()
#             carro.para()

#RESUMINDO:

# if carro.esquerda():
#     bloco1
# elif carro.direita():
#     bloco2
# elif carro.ré():
#     bloco3
# else:
#     bloco4

#Obs.: DENTRO DO "if" posso usar quantos "elif" eu quiser, não há limites.
#      O "else", posso usar uma ou nenhuma vez.


########################################################################################################################
#########################################################   PRÁTICA   ##################################################
########################################################################################################################

#   ESTRUTURA CONDICIONAL COMPOSTA   #

nome = str(input('Qual é o seu nome?')).strip()
if nome == 'William':
    print('Que nome bonito!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

#   ESTRUTURA CONDICIONAL COMPOSTA ANINHADA  #

nome = str(input('Qual é o seu nome?')).strip()
if nome == 'William':
    print('Que nome bonito!')
elif nome == 'Spyke' or nome == 'Maggie' or nome == 'Belulu' or nome == 'Sophia':
    print('Seu nome é legal.')
elif nome in 'Ana Victória Caroline Andressa':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))