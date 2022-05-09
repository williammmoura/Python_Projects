#Author: William Monte de Moura
#Aula: 12

#   Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre
#seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso;
#– Entre 18,5 e 25: Peso Ideal;
#– 25 até 30: Sobrepeso;
#– 30 até 40: Obesidade;
#– Acima de 40: Obesidade Mórbida.

#Inserindo dados:
peso = float(input('Qual é a sua peso (Kg)?'))
h = float(input('Qual é a sua altura (em METROS)?'))

#Calculo do IMC:
imc =  peso / h**2

print('Seu IMC (Índice de Massa Corporal) é igual a {:.2f}.'.format(imc))

#Condições:
if imc < 18.5:
    print('Você está abaixo do peso recomendado.')
elif 18.5 <= imc < 25:
    print('Você está com o peso ideal.')
elif 25 <= imc < 30:
    print('Você está com sobrepeso.')
elif 30 <= imc < 40:
    print('Cuidado! Você está com obesidade.')
elif imc >= 40:
    print('Muito cuidado! Você está com obesidade mórbida.')