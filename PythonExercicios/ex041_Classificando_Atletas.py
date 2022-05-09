#Author: William Monte de Moura
#Aula: 12

#   A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua ca-
#tegoria, de acordo com a idade:

#– Até 9 anos: MIRIM

#– Até 14 anos: INFANTIL

#– Até 19 anos: JÚNIOR

#– Até 25 anos: SÊNIOR

#– Acima de 25 anos: MASTER

from datetime import date

nasc = int(input('Ano de nascimento:'))
atual = date.today().year

#Idade:
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
#Condicional:
if idade < 9:
    print('Você está na categoria MIRIM.')
elif 9 <= idade <= 14:
    print('Você está na categoria INFANTIL.')
elif 15 <= idade <= 18:
    print('Você está na categoria JÚNIOR.')
elif 19 <= idade <= 24:
    print('Você está na categoria SÊNIOR.')
elif idade >= 25:
    print('Você está na categoria MASTER.')