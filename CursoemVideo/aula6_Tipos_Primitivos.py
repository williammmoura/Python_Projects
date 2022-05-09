#Variável interativa.
print('PARTE 1')
n1 = input('Digite um número:')
#Quero saber o "tipo primitivo".
print(type(n1))
#Deu "str", pois está envolvino nas áspas.

###Para especificar o tipo primitivo:###
print('PARTE 2')
n1 = int(input('Digite um número:'))
print('Tipo primitivo:')
print(type(n1))
print('Segue o que se pede.')
n2 = int(input('Digite outro (podendo ser o mesmo) número:'))
#### Fazendo a soma dos dois números digitados: ####
soma = n1 + n2
#print('O valor, da soma (',n1,'+',n2,'), dos números digitados é: {}'.format(soma))
print('O valor, da soma ({} + {}), dos numeros digitados é: {}'.format(n1, n2, soma))



########################################################################################################################



####Repare que foi colocado o "int"(inteiro), assim aparece como número inteiro.
#### OBS.:Existem outros "tipos primitivos".####
#### int = inteiro (7, 2, -1, 2020,,,);
#### float = reais (pontos flutuantes) (7.0, 6.54, -12.524, ...);
#### bool = valores lógicos ou booleanos (Só aceita valores True (Verdadeiro) ou False (Falso));
#### str = valor caracter ou strengs ('OLá', '7.5', '', ...).




########################################################################################################################
################################################### Concatenação #######################################################
########################################################################################################################
print('PARTE 3')
print('Aqui teremos um exemplo de concatenação.')
n01 = input('Digite um número:')
n02 = input('Digite outro número (podendo ser o mesmo que foi digitado):')
s = n01 + n02
print('O programa apresentará {}'.format(s),', que é a concatenação ("junção") dos dois números digitados.')

print('###### Observar o script! #######')



########################################################################################################################
##################################################   TESTE LÓGICO   ####################################################
########################################################################################################################

w = input('Digite algo:')
print(w.isnumeric())