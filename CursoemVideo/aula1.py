#Author: William Monte de Moura
#Title: Aula 1 - Python


################################################################################
########################  Usar o comando 'print'  ##############################
################################################################################

#Explicação: O comando 'print' é o mesmo que escrever em tela. O sintaxe
#será usado da seguinte forma:
print('Caracter')
#Variações do comando 'print':
#junção de duas "mensagens".
print('Caracter'+'Caracter2')  #OBS.: O sinal de + pode ser substituído por
#vírgula (,), isso dependerá do contexto do programa.

################################################################################
########################## Operadores matemáticos ##############################
################################################################################

#As operações básicas de matemática, são representados por (*,/,+,-) multi
#plicação, divisão, soma, subtração reespectivamente.
#Exemplos:
5*5
81/3
4+4
1240-1230

################################################################################
############################### Criando variáveis ##############################
################################################################################

#Para criar uma variável é necessário dar um nome para ela e um valor lógico.
#Esse valor pode ser números ou caracteres (letras).
nome = 'William'
idade = 28
peso = 60
dia = 2
mes = 'Março'
ano = 1992
print (nome, idade, peso, dia, mes, ano)

  #Para criar uma variável INTERATIVA devemos colocar, após o sinal de igualdade,
  #o comando input (entrada).
  #Exemplo:

from time import sleep

nome = input('Qual é o seu nome?')
print('Olá,'+nome+'!' + 'Prazer em te conhecer!')
dia = int(input('Qual é a dia (XX) do seu nascimento?'))
mes = int(input('Qual é o mês (XX) do seu nascimento?'))
ano2 = int(input('Qual é o ano (XXXX) do seu nascimento?'))
idade2 = 2020 - ano2
print('Sua idade é:')
print(idade2)
peso = input('Qual é o seu peso (Kg)?')
print('Conferindo dados...')
sleep(3)
print(nome,',',idade2, 'ano(s);',' Peso atual:', peso + 'Kg.')