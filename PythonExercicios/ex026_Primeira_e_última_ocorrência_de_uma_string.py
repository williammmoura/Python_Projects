#Author: William Monte de Moura
#Aula: 9

#Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A";
# - Em que posição ela aparece a primeira vez;
# - Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase:')).strip().upper()     ####"upper" coloca toda frase em maiúscula.####
print('A letra "a"("A") aparece {} vezes.'.format(frase.count('A')))

#### OBS.: Os espaços, entre as palavras, contam.####

print('A primeira vez em que a letra "a"("A") apareceu foi na posição {}.'.format(frase.find('A')+1))
#### O "+1" corrige a leitura do programa, onde, o programa considera, como a primeira letra, no espaço zero. Colocando
# "+1" temos a primeira letra na posição onde ela realmete está.####

print('A última vez em que a letra "a"("A") apareceu foi na porsição {}.'.format(frase.rfind('A')+1))
#### O "rfind()" procura a partie da direita para esquerda####