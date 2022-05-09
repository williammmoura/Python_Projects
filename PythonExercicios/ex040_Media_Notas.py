#Author: William Monte de Moura
#Aula: 12

#   Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
#média atingida:

#– Média abaixo de 5.0: REPROVADO

#– Média entre 5.0 e 6.9: RECUPERAÇÃO

#– Média 7.0 ou superior: APROVADO


nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))

media = (nota1 + nota2) / 2
exame = 10 - media

if media < 5.0:
    print('Você ficou com a média {:.2f}. Logo, você está REPROVADO.'.format(media))
elif 5.0 <= media <= 6.9:
    print('Você ficou com a média {:.2f}. Logo, terá que fazer o EXAME FINAL.'.format(media))
    print('Você terá que somar {:.2f} para ser aprovado.'.format(exame))
elif media >= 7.0:
    print('Você ficou com a média {:.2f}. Você está APROVADO. Parabéns!'.format(media))