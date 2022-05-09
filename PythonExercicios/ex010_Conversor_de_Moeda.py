#Author: William Monte de Moura
#Aula: 7

#Crie um programa que leia quanto dinheiro tem na carteira e mostre quantos Dólares ela pode comprar.
#Considere US$1,00 = R$5,515 (Dólar Comercial 28/04/20).

real = float(input('Quanto(s) Real(is) você tem em sua carteira? R$'))
d = real / 5.515
e = real / 5.974
print('Você poderá comprar US${:.3f} e €{:.3f}'.format(d, e))

#OBS.: ":.3f" limitei o número de casas decimais flutuantes.


