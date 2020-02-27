""""" 040 - Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final de acordo
com a media atingida:
-Media abaixo de 5.0: REPROVADO
-Media entre 5.0 e 6.9:RECUPERACAO
-Media acima de 7.0:APROVADO """


print(40*'\033[1:33m=\033[m')
print('\033[1:33mVamos saber se voce foi aprovado?\033[m')
print(40*'\033[1:33m=\033[m')
nome = str(input('Digite o nome do aluno : '))
n1 = float(input('Digite a primeira nota : '))
n2 = float(input('Digite a segunda nota : '))

media = (n1 + n2) / 2
if media < 5.0 :
    print('Ola {}.\nInfelizmente voce foi REPROVADO. Sua media foi {:.1f} e a minima media para evitar e de 5.0 '.format(nome,media))
elif media <= 6.9:
    print('Ola {}.\nVoce foi enviado pra RECUPERACAO.Sua media foi de {:.1f}.'.format(nome,media))
else:
    print('Parabens {}.Voce foi aprovado!! Sua media foi de {:.1f}'.format(nome,media))