########################################################################################################################
########################################   MANIPULANDO CADEIAS DE TEXTOS   #############################################
########################################################################################################################

#   Cadeia de texto = string (str).
#   Para o Python, os textos estão SEMPRE em aspas simples OU duplas (há a possíbilidade de três aspas simples).

# Exemplo:
frase = 'Curso em Vídeo Python.'
#   O que está escrito, em cima, é uma string. Essa string está associada a uma variável, ou seja, cada letra e espaços
# entre as letras, ocupam um micro-espaço na memória do computador (a frase, toda, ocupa um espaço de memória).
#   Na frase associada a variável "frase", ocupa 21 micro-espaços na memória (pois a sequencia numérica começa em zero).
print(frase)
print('Tudo o que está aparecendo na tela (frases e textos) é uma, ou várias, strings.')

########################################################################################################################
#################################################   FATIAMENTO   #######################################################
########################################################################################################################

#   O símbolo de colchetes é o identificador de estrutura de dado, chamado "LISTA".

# Exemplo:
#   Aqui, o programa irá escrever apenas o caracter 9 da variável "frase".
print(frase[9])
#   O resultado do programa, será mostrar a letra "V", que é o nono micro-espaço, de memória, onde está alocado "V".

#  1) Outra maneira de fatiar:
print(frase[9:13])
#   O resultado será mostrar a letra "Vide". A letra "o", que é o 13º micro-espaço, será excluído.
###  SEMPRE um à menos no final.  ###
print(frase[9:25])

#  2) Outra maneira de fatiar.
print(frase[9:21:2])
#   O resultado que será mostrado será o mesmo mostrado a cima, porem pulando de 2 em 2. Esse é o signoficado do 2!
#   O resultado que irá aparecer na tela será: "VdoPto".

#  3) Outra maneira de fatiar.
print(frase[:5])
#   O resultado que será mostrado na tela será: "Curso".
#   Sem o número de início, o programa entende que deverá começar pelo início da frase.

#  4) Outra maneira de fatiar.
print(frase[15:])
#   O resultado que será mostrado na tela será: "Python."
#   Sem o número do final, o programa entende que deverá terminar no final da frase. Bom usar quando não se sabe o últi-
# mo caractere.

#  5) Outra maneira de fatiar.
print(frase[9::3])
#   O resultado que será mostrado será o mesmo mostrado a cima, porem pulando de 3 em 3. Esse é o signoficado do 3!
#   Como não foi colocado nenhum valor "no meio", o progama entende, que não há limitação para a fatia no final.
#   O resultado que irá aparecer na tela será: "VePh.".


########################################################################################################################
######################################################   ANÁLISE   #####################################################
########################################################################################################################

#   Vamos usar a função "len".
#   A função "len" mostra mostra o comprimento da string (frase, texto).
print(len(frase))

#   1) Outra maneira de analisar.
print(frase.count('o'))
#   Aqui, peço para o programa contar quantos "o" (minúsculo) tem na frase.
print(frase.count('o',0,13))
#   Aqui mostra quantos "o" têm do micro-espaço 0 até o micro-espaço 12 (lembrando que o programa irá excluir o 13º).

#   2) Outra maneira de analisar.
print(frase.find('deo'))
#   Aqui o programa irá procurar os micros-espaços que contenham o "deo".
#   Na tela aparecerá "11", que é o momento que começou o "deo".
print(frase.find('android'))
#   Na tela aparecerá "-1", que quer dizer, que a string fornecida não existe na frase analisada.

#   3) Outra maneira de analisar.
print('Curso' in frase )
#   Na tela aparecerá "True", que quer dizer ,que a string fornecida existe na frase analisada.
print('curso' in frase)
#   Na tela aparecerá "False", que quer dizer, que a string fornecida não existe na frase analisada.
#   Lembrando! O Python faz a diferença entre letras maiúsculas e minúsculas.

#####################   OBS.: O "in" é um operador, mas também pode ser usado para fazer análise.   ####################


########################################################################################################################
####################################################   TRANSFORMAÇÃO   #################################################
########################################################################################################################

print(frase.replace('Python', 'Android'))
#   Na tela aparecerá na frase, que originalmente estava a palavra "Python", agora aparece "Android".
#   Substitui em uma forma secundária.

#   1) Outra maneira de transformação.
print(frase.upper())
#   Na tela aparecerá toda a frase em maiúsculo.
print(frase.lower())
#   Na tela aparecerá toda a frase em minúsculo.

#   2) Outra maneira de transformação.
print(frase.capitalize())
#   O "capitalize" joga todos os caracteres para minúsculo e só o primeiro caracter vai ficar em maiúsculo.

#   3) Outra maneira de transformação.
print(frase.title())
#   O "title" analisa quantas palavras tem na frase. Ele verifica onde há espaços, fazendo assim a quebra de palavras.
#Ou seja, é capitalize palavra por palavra.
#   Na tela aprecerá "Curso Em Vídeo Python."

frase2 = '   Aprenda Python  '
print(frase2.strip())
#   Aqui será removido todos os espaços inúteis.
#Contra exemplo:
print(frase2)
#   Compare na tela.

#   4) Outra maneira de transformação.
print(frase2.rstrip())
#   Aqui será removido todos os espaços inúteis do lado direito (r = rigth = direita).
#   De forma análoga...
print(frase2.lstrip())
#   Remove todos os espaços inúteis do lado esquerdo (l = left = esquerda).


########################################################################################################################
###################################################   DIVISÃO   ########################################################
########################################################################################################################

print(frase.split())

#   ESTUDAR AS OUTRAS FUNCIONALIDADES DO "split()".
#   Por padrão é feito nos espaços. Ele cria uma divisão, ou seja, ele cria novas strings com as palavras que compoem a
#frase.
#   Na tela aparecerá: ['Curso', 'em', 'Vídeo', 'Python.']
#   Na tela aparece um lista com as palavras existentes na frase.
#   A palavra 0 = Curso;
#   A palavra 1 = em;
#   A palavra 2 = Vídeo;
#   A palavra 3 = Python.


########################################################################################################################
###################################################   JUNÇÃO   #########################################################
########################################################################################################################

print('-'.join(frase))
#   Na tela: C-u-r-s-o- -e-m- -V-í-d-e-o- -P-y-t-h-o-n-.


########################################################################################################################
########################################################################################################################

print('''Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o 
Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(),
title(), strip(), junção com join().''')

###########################   FAZENDO TESTES   #############################

frase3 = 'Curso em Vídeo Python.'
frase3 = frase3.replace('Python', 'Android')
print(frase3)
#   Na tela: "Curso em Vídeo Android."

dividido = frase.split()
print(dividido[0])
#   Na tela: "Curso"

dividido = frase.split()
print(dividido[2][3])
#   Na tela: "e"