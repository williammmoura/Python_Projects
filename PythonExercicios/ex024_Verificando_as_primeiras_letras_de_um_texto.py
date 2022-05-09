#Author: William Monte de Moura
#Aula: 9

#Crie um programa que leia o nome de uma cidade e diga se ela começa, ou não, com a palavra "Santa".

cid = str(input('Em que cidade você nasceu?')).strip().split()


########################################################################################################################

##############################################   .split()   ############################################################

#Por padrão é feito nos espaços. Ele cria uma divisão, ou seja, ele cria novas strings com as palavras que compoem a
#frase.
#   Na tela aparecerá: ['Curso', 'em', 'Vídeo', 'Python.']
#   Na tela aparece um lista com as palavras existentes na frase.
#   A palavra 0 = Curso;
#   A palavra 1 = em;
#   A palavra 2 = Vídeo;
#   A palavra 3 = Python.

########################################################################################################################


print(cid[0].lower() == 'santa')

####  OBS.: Pode ser usado tanto o ".upper()" quanto o ".lower()". Desde que esteja correspondente a forma que foi es-
#crita na correspondencia (==).