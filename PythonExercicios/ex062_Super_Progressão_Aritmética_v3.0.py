#Author: William Monte de Moura
#Aula: 14

#   Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando
#ele disser que quer mostrar 0 termos.

print('Dez primeiros termos de uma Progressão Aritmética (PA).')

#Variáveis:
t = int(input('Digite o primeiro termo da PA:'))
r = int(input('Digite a razão da PA:'))

#Contador:
termo = t # Será contado o primeiro termo, fornecido pelo usuário, sempre somando a razão (r).
cont = 1 #Contador para condição de parada (segundo while). Aqui sendo menor/igual a total.
total = 0 #Contador para informar, ao usuário, quantos termos foram mostrados (texto mostrado no final do programa).
tm = 10 #Contador partido do décimo termo mostrado. Agregando ao "pedido" do usuário para mostrar mais termos.

#Primeiro "while" é para fazer (conforme o usuário) mostras mais termos da PA.
while tm != 0:
    total = total + tm  #Total mais o termo adicional fornecido pelo usuário.
    while cont <= total:
        print('{} → '.format(termo), end='')
        #Conta da PA:
        termo = termo + r
        cont += 1
    print('PAUSA.')
    tm = int(input('Quantos termos você quer mostrar a mais?'))
    #if tm == str():
    #    print('Opção INVALIDA!')
print('')
print('Progreção finalizada com {} termos mostrados na tela.'.format(total))
