#Aula Sobre operadores aritméticos.


########################################################################################################################
###########################################   Operadores Aritméticos:   ################################################
########################################################################################################################

# + -> ADIÇÃO;
# - -> SUBTRAÇÃO;
# * -> MULTIPLICAÇÃO;
# / -> DIVISÃO;
# ** -> POTENCIAÇÃO;
# // -> DIVISÃO INTEIRA;
# % -> MÓDULO OU RESTO DA DIVISÃO.

5 + 2==7
5 - 2 ==3
5 * 2 ==10
5 / 2 ==2.5
5 ** 2 ==25
5 // 2 ==2
5 % 2 ==1

#OBS.: Os == são para testar se uma coisa é IGUAL a outra. Já = é sinal de ATRIBUIÇÃO.


########################################################################################################################
##############################################   Ordem de Precedência   ################################################
########################################################################################################################

# 1º) () *PARENTESES*
# 2º) **
# 3º) *, /, //, %
# 4º) + e -


########################################################################################################################
#####################################################   Exemplos   #####################################################
########################################################################################################################

5 + 3 * 2 == 11
3 * 5 + 4 ** 2 == 31
3 *(5 + 4)** 2 == 243

#OBS. 1: RAIZ QUADRADA -> 81**(1/2)
#        RAIZ CÚBICA -> 27**(1/3)

#OBS. 2: Multiplicando string:
#        'Oi' * 5 == OiOiOiOiOi





########################################################################################################################
####################################################   Prática   #######################################################
########################################################################################################################

nome = str(input('Qual é o seu nome?'))
#Aqui, vou escrever o nome usando 20 espaços. Por isso no script tenho {:20}.
print('Prazer em te conhecer, {:20}!'.format(nome))
#Repare que a rodar o programa, a esclamação ficará distante do nome. Isso por que usou 20 espaços (contados os do nome)
#para escrever na tela.


#Esse recurso é importante para usar ALINHAMENTOS.
#    Exemplo:
print('Prazer em te conhecer, {:>20}!'.format(nome))
print('Prazer em te conhecer, {:^20}!'.format(nome))

########### Aqui podemos colocar qualquer sinal ({:=^20}, {:+^20}, ...).
print('Prazer em te conhecer, {:=^20}!'.format(nome))


########################################################################################################################
########################################################################################################################

n1 = int(input('{}, digite um valor:'.format(nome)))
n2 = int(input('Digite outro valor (podendo ser o mesmo digitado anteriormente):'))
soma = n1 + n2
mult = n1 * n2
div = n1 / n2
dinteira = n1 // n2
resdiv = n1 % n2
sub = n1 - n2
exp = n1 ** n2

print('A soma é igual a: {}, '.format(soma), end='')

#OBS.: Note, que acima foi usado ", end='' ", esse comando mantem na mesma linha.

print('A multiplicação é igual a: {}'.format(mult))
print('A divisão é igual a: \n {}'.format(div))

#OBS.: Acima temos o "\n", que quebra a linha.

print('A divisão inteira é igual a: {}'.format(dinteira))
print('O resto da divisão é: {}'.format(resdiv))
print('A subtração é igual a {}'.format(sub))
print('A potenciação é igual a: {}'.format(exp))