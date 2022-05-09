#Author: William Monte de Moura
#Aula: 14

#   Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a di-
#gitação novamente até ter um valor correto.

#Adicionando dados:
print('''[ M ] -> Masculino;
[ F ] -> Feminino.''')
sexo = str(input('Informe seu sexo [M/F]:')).strip().upper()[0]  #Adicionado o 0 para pegar somente a primeira letra

#Condição para validação:
while sexo not in 'MmFf':
    sexo = str(input('''DADO INVALIDO! Digite APENAS "F" ou "M" (F -> feminino / M -> masculino):''')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))