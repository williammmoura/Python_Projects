#Author: William Monte de Moura
#Arithmetic Average

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
n3 = float(input('Digite a terceira nota:'))
m = (n1 + n2 + n3) / 3

print('A sua média foi: {:.2f}'.format(m))
if m >= 7.00:
    print('Sua média foi {:.2f}, logo você está aprovado. Parabéns'.format(m))
else:
    print('Sua média foi {:.2f}. Você terá que realizar o exame final. Bons Estudos.'.format(m))