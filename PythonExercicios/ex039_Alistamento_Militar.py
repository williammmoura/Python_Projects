#Author: William Monte de Moura
#Aula: 12

#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se ali
#star ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também
# deverá mostrar o tempo que falta ou que passou do prazo.

#Importando da bibloteca "datetime".
from datetime import date
from time import sleep

#Criando uma variável para importar a data atual.
atual = date.today().year
frase = 'Alistamento Militar'
print('\033[46m-\033[m' * 70)
print(frase)
print('\033[46m-\033[m' * 70)
print('[ 1 ] -> Masculino;')
print('[ 2 ] -> Feminino.')
print('Digite o seu sexo conforme as numerações relacionadas.')
sexo = int(input('Sexo:'))

#Condicional para idade:
if sexo == 1:
    print('Aguarde...')
    sleep(2)
    ano = int(input('Em qual ano você nasceu?'))
    # Idade:
    idade = atual - ano
    # Quanto anos faltam.
    xanos = 18 - idade
    # Quantos anos passaram.
    yanos = idade - 18
    # Ano do alistamento (futuro e passado, reespectivamente).
    anoalis1 = atual + xanos
    anoalis2 = atual - yanos
    if idade < 18 and sexo == 1:
        print('Você tem mais \033[1;30;42m{} ano(s)\033[m para fazer o alistamento militar obrigatório.'.format(xanos))
        print('Seu alistamento será em {}.'.format(anoalis1))
    elif idade == 18 and sexo == 1:
        print('Você \033[1;30;43mprecisa fazer\033[m o alistamento militar obrigatório \033[1;30;43mNESTE ANO.'
          ' CORRE LÁ!\033[m')
    elif idade > 18 and sexo == 1:
        print('Você já \033[1;30;41mdeveria ter feito\033[m o alistamento militar obrigatório \033[1;30;41mhá {} ano(s)!'
          '\033[m'.format(yanos))
        print('Você deveria ter feito o alistamento em {}.'.format(anoalis2))
elif sexo == 2:
    ano2 = print('Você não é obrigada a fazer o alistamento.')