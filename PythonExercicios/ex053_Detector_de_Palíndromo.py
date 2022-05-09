#Author: William Monte de Moura
#Aula: 13

#   Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de
#palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

# Já coloco ".strip()" e ".upper()" para não ter problemas de espaços EXTERNOS vagos, deixados pelo o usuário, e colocar
#em letras maiúsculas para efeito de comparação.
frase = str(input('Digite uma paralavra, ou uma pequena frase: ')).strip().upper()

# Fazendo tratamento de strings:
# Usando ".split()" para separar as palavras da frase (gerar uma lista).
palavras = frase.split()
# Usando ".join()" para juntar as palavras sem espaços entre elas ('').
junto = ''.join(palavras)

# Gerar a string inversa:
inverso = ''

# Usando o "for" pegando da última até a primeira letra, "len(junto)-1", pegando até a primera letra (que na lista é 0),
#"-1", indo do final para o início, "-1"
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Essa frase (palavra) É UM PALÍNDROMO.')
else:
    print('Essa frase (palavra) NÃO É UM PALÍNDROMO.')