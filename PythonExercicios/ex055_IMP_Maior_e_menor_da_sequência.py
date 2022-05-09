#Author: William Monte de Moura
#Aula: 13

#    Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.


###################################################   IMPORTANTE   #####################################################
####   ANÁLISE DE DADOS. PODE SER FEITO ESTATÍSTICA!   ###


#Fazendo o intervalo dos valores de peso:
maior = 0    ### Poderia colocar um valor, superior, de 9999.99 .
menor = 0

for p in range(1, 6):
    peso = float(input('Peso(Kg) da {}ª pessoa:'.format(p)))
    if p == 1: #Leitura do peso da primeira pessoa. Ele será o maior e o menor peso.
               #Não há outro comparartivo até aqui.
        maior = peso
        menor = peso
    else:
    if peso > maior:  #Aqui começa a comparar com os pesos lidos.
                          #Compara com o 1º, 2º, 3º... pesos.
        maior = peso
    if peso < menor:
        menor = peso
print('O MAIOR peso lido foi de {}.'.format(maior))
print('O MENOR peso lido foi de {}.'.format(menor))