#Author: William Monte de Moura
#Aula: 13

#   Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print('Contagem de Números Pares')

for contpar in range(0, 51, 2):
    print(contpar, end=', ',)
print('Acima está todos os números pares de 0 a 50.')