# Aqui converto um valor "string" para "float".
n = float(input('Digite um valor:'))
print(n)


########################################################################################################################
####################### Aqui veremos se o argumento é verdadeiro ou falso (usando o ".is...") ######################
########################################################################################################################
n = (input('Digite algo:'))
### Usando o método ".isnumeric", quero saber se é possível converter o argumento (str) digitado em um numérico:
print(n.isnumeric())

n = (input('Digite algo:'))
### Usando o método ".isnalpha", quero saber se é possível converter o argumento (str) digitado em uma letra:
print(n.isalpha())

n = (input('Digite algo:'))
### Usando o método ".isnalnum", quero saber se é possível converter o argumento (str) digitado em um alpha-numérico:
print(n.isalnum())

n = (input('Digite algo:'))
### Usando o método ".isupper", quero saber se os argumento (str) digitado estão em maiúsculo:
print(n.isupper())
