#Author: William Monte de Moura
#Aula: 15

#   Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
#999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (descon-
#siderando o flag).

soma = quant = 0
while True:
    n = int(input('Digite um número inteiro (O NÚMERO 999 FINALIZA O PROGRAMA):'))
    if n == 999:
        break
    soma += n
    quant += 1   #"quant" colocado aqui, após o break, para não contar o flag.
print(f'A quantidade de número digitados foi {quant} e a soma dos valores (desconsiderando 999) é {soma}.')