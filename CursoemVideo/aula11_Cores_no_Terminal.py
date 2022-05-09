########################################################################################################################
#################################################   Cores no Terminal   ################################################
########################################################################################################################

##########################################    Código ANSI (escape sequence)   ##########################################

#   O código ANSI, para cores,  começa com "\" (contrabarra) e depois vem o código.
#   Sempre que quiser representar uma cor, em PYTHON, será: \033[codigodacorm

#Ex.: \033[style;text;backm

#style -> estilo;            O estilo do texto (sublinhado, negrito, itálico...)
#text -> texto;              Cor do texto
#back -> background (fundo). Cor do fundo

# \033[0;33;44m -> Código de cor

#Códigos para estilo: 0, 1, 4, 7.
# 0 -> Deixa o estilo default;
# 1 -> Negrito;
# 4 -> Sublinhado
# 7 -> Inverte as configuração (o que foi colocado de fundo passa para a letra e a letra para o fundo).

#Código para texto: 30, 31, 32, 33, 34, 35, 36, 37
# 30 -> Branco; (white)
# 31 -> Vermelho; (red)
# 32 -> Verde; (green)
# 33 -> Amarelo; (yellow)
# 34 -> Azul; (blue)
# 35 -> Lilás; (lilac)
# 36 -> Verde-água; (sea-green)
# 37 -> Cinza. (grey)

#Códigos para background (fundo): 40, 41, 42, 43, 44, 45, 46, 47.
# 40 -> Branco; (white)
# 41 -> Vermelho; (red)
# 42 -> Verde; (green)
# 43 -> Amarelo; (yellow)
# 44 -> Azul; (blue)
# 45 -> Lilás; (lilac)
# 46 -> Verde-água; (sea-green)
# 47 -> Cinza. (grey)


########################################################################################################################
##############################################################   TESTES   ##############################################
########################################################################################################################


# teste -> \033[0;30;41m
# teste -> \033[4;33;44m
# teste -> \033[1;35;43m
# teste -> \033[30;42m
# teste -> \033[m
# teste -> \033[7;30m


########################################################################################################################
############################################################   PRÁTICA   ###############################################
########################################################################################################################

print('\033[1;31;40mOlá, Mundo!')

print('\033[4;37;46mEstou bem')

print('\033[1;30;41mVamos, INTER!\033[m')

a = 5
b = 7
print('Os valores são \033[32;44m{}\033[m e \033[33;44m{}\033[m.'.format(a, b))

nome = 'William'
print('Olá! Muito prazer em te conhecer {}{}{}!'.format('\033[1;31;40m', nome, '\033[m'))

nome1 = 'William'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer {}{}{}!'.format(cores['amarelo'], nome, cores['limpa']))