#Author: William Monte de Moura
#Aula: 13

#   Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
#a maioridade e quantas já são maiores.


###################################################   IMPORTANTE   #####################################################
####   ANÁLISE DE DADOS. PODE SER FEITO ESTATÍSTICA!   ###


#Importação de biblioteca:
from datetime import date

# Fazendo um contador para ver quantas pessoas são de maior e de menor, reespectivamente:
totmaior = 0
totmenor = 0

# Usando o "for" para ler o ano de nascimento de 7 pessoas.
for c in range(1, 11):
    anonasc = int(input('Pessoa {} -> Qual é o ano de seu nascimento:'.format(c)))
    atual = date.today().year
    idade = atual - anonasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('')
print('Ao todo tivemos {} pessoa(s) maiore(s) de idade.'.format(totmaior))
print('Ao todo tivemos {} pessoa(s) menore(s) de idade.'.format(totmenor))
print('')

#Representação em porcentagem:
estmaior = (totmaior * 100) / 10
estmenor = (totmenor * 100) / 10

print('Maior de idade: {}%'.format(estmaior))
print('Menor de idade: {}%'.format(estmenor))