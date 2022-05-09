#Author: William Monte de Moura
#Aula: 12

#   Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pa-
#gamento:
#– à vista dinheiro/cheque: 10% de desconto;
#– à vista no cartão: 5% de desconto;
#– em até 2x no cartão: preço formal;
#– 3x ou mais no cartão: 20% de juros.

print('{:=^40}'.format(' Lojas Moura ')) #Nome da loja com formatação centralizado.

#Dados:
v = float(input('Qual é o valor do produto? R$'))
print('FORMAS DE PAGAMENTOS:')
print('[ 1 ] -> Dinheiro/cheque;')
print('[ 2 ] -> cartão (à vista);')
print('[ 3 ] -> Cartão (em até 2x);')
print('[ 4 ] -> Cartão (3x ou mais).')
op = int(input('Digite o número da opção de pagamento mostrado acima:'))

#Calculos:
#Descontos:
dez = v - ((v * 10) / 100)
cinco = v - ((v * 5) / 100)
#Valor em 2x:
duasx = v / 2

#Condições:
if op == 1:
    print('Com desconto de 10%, o valor inicial de R${}, agora passa ser de R${:.2f}.'.format(v, dez))
elif op == 2:
    print('Com desconto de 5%, o valor inicial de R${}, agora passa ser de R${:.2f}.'.format(v, cinco))
elif op == 3:
    print('O valor {} será dividido em duas parcelas de {:.2f}.'.format(v, duasx))
########################################################################################################################
###################################################   IMPORTANTE   #####################################################
########################################################################################################################
elif op == 4:
    # Acréssimo:
    vinte = v + ((v * 20) / 100)
    parc = int(input('Em quantas parcelas?'))
    # Parcelas:
    tot = vinte / parc
    print('O valor de R${:.2f}, dividido em {} vezes, será de R${:.2f} mensais.'.format(v, parc, tot))
    print('Com um acréssimo de 20% o valor final será de R${:.2f}.'.format(vinte))
else:
    print('\033[1;30;41mOPÇÃO INVALIDA! Tente novamente.\033[m')