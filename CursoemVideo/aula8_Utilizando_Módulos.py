# Utilizando Módulo

#Vamos usar o comando "import", logo no início do script, para carregar o módolo (biblioteca para o programa que será
#feito.

####################################################   Exemplo   #######################################################
 #Vamos supor que temos alguns módulos:
 #Comida: Arroz, feijão, batata, tomate...
 #Doces: Açucar, brigadeiro, bolo, pudim...
 #Bebidas: Água, refri, suco, cerveja...

#Para buscar esse módulos e todas as suas funcionalidades, usaremos a seguinte sintaxe:
#"import bebida"
#Para buscar uma funcionalidade desse módulo, a sintaxe fica:
#"from doce import pudim"

################################################   Exemplo Prático   ###################################################
#import math  #Importei o módulo math (módulo matemático), ou seja, posso usar todas as funcionalidades desse módulo.

#ceil  #Arredondamento para cima;
#floor #Arredondamento para baixo;
#trunc #Elimina os números após a vírgula (ele irá truncar o número);
#pow   #Similar ao **, que é potência;
#sqrt  #Calcula a raiz quadrada;
#factorial #Calcula o fatorial de um número (lembrando: 20!)

#from math import sqrt  #Aqui, importei uma única funcionalidade do módulo math.

#from math import sqrt, ceil  #Aqui, importei duas funcionalidades do módulo math.



########################################################################################################################
###################################################   PRÁTICA   ########################################################
########################################################################################################################



#import math
#num = int(input('Digite um número:'))
#raiz = math.sqrt(num)
#print('A raiz de {} é igual a {:.2f}'.format(num, raiz))


########################################################################################################################


#from math import sqrt, floor
#num = int(input('Digite um número:'))
#raiz = sqrt(num)
#print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))


########################################################################################################################


#import random   ##Nessa biblioteca, posso gerar números aleatórios (entre 0 e 1, ou seja, um float).
#num = random.random()
#print(num)


########################################################################################################################


#import random
#num = random.randint(1, 10)  #Aqui defini o intervalo de números (inteiros) que podem ser gerados pelo computador
#print(num)


########################################################################################################################


import emoji
print(emoji.emojize('Olá, Mundo! Use -> :mask:', use_aliases=True))