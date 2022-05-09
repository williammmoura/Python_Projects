#Author: William Monte de Moura
#Aula: 10


#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
#foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

from termcolor import colored

velocar = float(input('Qual é a velocidade (Km/h) do seu carro?'))
multa = (velocar - 80)*7
if velocar > 80:
    print(colored('MULTADO! Você está acima da velocidade limite. Sua multa será de R${:.2f}.','red').format(multa))
else:
    print(colored('Você está dentro da velocidade permitida. Dirija com segurança!','green'))