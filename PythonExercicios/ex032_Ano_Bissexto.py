#Author: William Monte de Moura
#Aula: 10

#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date  #Importar a biblioteca "datetime" para o Python trazer a data de hoje.

ano = int(input('Qual ano você quer analisar? Coloque 0 para analisar o ano atual:'))

#Representando o zero como o ano atual.
if ano == 0:
    ano = date.today().year #Pega o ano atual que está configurado na máquina.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  #TRADUZINDO: O ano tem que ser divisível por 4 e, também pode ser
# divisível por 100, não podendo ser diferente de zero, ou o ano ser divisível por 400.
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))