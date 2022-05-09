#Author: William Monte de Moura
#Aula: 6 (Primitives Types and Data Output)

#3) Crie um programa que leia dois números e mostre a soma entre eles.

#Aqui, foi colocado um tipo primitivo "int". Ou seja, será convertido para um número inteiro.
num = int(input('Digite um número:'))
num2 = int(input('Digite um numero (pode ser qualquer número, até mesmo o que você digitou anteriormente):'))
soma = num + num2
print('A soma desses dois números, que você digitou, é:',soma,'.')


#### OBS.:Existem outros "tipos primitivos".####
#### int = inteiro (7, 2, -1, 2020,,,);
#### float = reais (pontos flutuantes) (7.0, 6.54, -12.524, ...);
#### bool = valores lógicos ou booleanos (Só aceita valores True (Verdadeiro) ou False (Falso));
#### str = valor caracter ou streans ('OLá', '7.5', '', ...).


#######Utilizando o ".format()".
print('A soma entre {} e {} que você digitou, é:{}'.format(num,num2,soma))