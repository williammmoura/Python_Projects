#Author: William Monte de Moura
#Aula: 13

#   Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
#grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

###################################################   IMPORTANTE   #####################################################
####   ANÁLISE DE DADOS. PODE SER FEITO ESTATÍSTICA!   ###

#Contador para soma da idade:
somaidade = 0
#Contador para a média da idade:
mediaidade = 0

#Verificar qual é a maior idade do homem e o nome:
maiorih = 0
nomevelho = ''

#Verificar quantas mulheres têm menos de 20 anos:
totm20 = 0

# Inserir dados:
for p in range (1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome:'.format(p))).strip()
    idade = int(input('Idade:'.format(p)))
    sexo = str(input('Sexo [M/F]:'.format(p))).strip()
    #Soma das idade para o cálculo da média:
    somaidade += idade   #somaidade = somaidade + idade

    #Maior idade do homem:
    if p == 1 and sexo in 'Mm':
        maiorih = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorih:
            maiorih = idade
            nomevelho = nome

    #Mulheres menores de 20 anos:
    if sexo in 'Ff' and idade < 20:
                totm20 += 1

#Calculo da média de idade:
mediaidade = somaidade / 4    #Aqui temos a MÉDIA!

print('A média de idade do grupo foi: {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorih, nomevelho))
print('Ao todo é(são) {} mulheres com menos de 20 anos.'.format(totm20))