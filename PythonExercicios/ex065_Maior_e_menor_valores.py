#Author: William Monte de Moura
#Aula: 14

#   Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
#valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a
#digitar valores.

soma = cont = media = maior = menor = 0
r = 'S'
while r == 'S':  #Feito pela primeira vez no jogo JOKENPÔ.
    n = int(input('Digite um número inteiro:'))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Você deseja digitar mais números [S/N]?')).upper().strip()[0] #Jogar o caracter para maiúsculo (.upper()),
#ignorar os espaços (.strip()) e considerar a primeira letra.
media = soma / cont
print('Você digitou {} números e a média dos valores digitados é {:.2f}.'.format(cont, media))
print('O menor número foi {} e o maior número foi {}.'.format(menor, maior))