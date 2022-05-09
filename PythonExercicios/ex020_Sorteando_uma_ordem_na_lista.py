#Author: William Monte de Moura
#Aula: 8

#O mesmo professor, do exercício anterior, quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um progra-
#ma que leia o nome, dos quatro aluno, e mostre a ordem sorteada.

import random
n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno:'))
n4 = str(input('Quarto aluno:'))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação dos trabalhos será:')
print(lista)
### OBS.: "shuffle" é igual a embaralhe a sequência.