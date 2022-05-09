#Author: William Monte de Moura
#Aula: 10

# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superio -
# res a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

s = float(input('Qual é o valor mensal do seu salário? R$'))
raj1 = s + ((s * 15) / 100)
raj2 = s + ((s * 10) / 100)
if s <= 1250.00:
    print('O salário de R${} contará com um acréscimo de 15%, ficando com o valor final de R${:.2f}.'.format(s, raj1))
else:
    print('O salário de R${} contará com um acréscimo de 10%, ficando com o valor final de R${:.2f}.'.format(s, raj2))