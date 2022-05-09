#Author: William Monte de Moura
#Aula: 9

#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Escreva seu nome completo:')).strip()
dividido = nome.split()
print('Muito prazer em te conhecer!')
print('O seu primeiro nome é: {}.'.format(dividido[0]))
print('O seu último nome é: {}.'.format(dividido[len(dividido)-1]))

### Usando "len(dividido)" eu irei saber quantas posições tem "dividido". Então "dividido[len(dividido)-1]", o "-1" é pa
#ra compensar o espaço inicial, que para o programa é zero, e fazer a contagem a partir do 1.