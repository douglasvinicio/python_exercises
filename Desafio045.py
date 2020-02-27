from random import randint
itens = ('PEDRA','PAPEL','TESOURA')
computador = randint(0, 2)
'''045 - Crie um programa que faca o computador jogar JOKENPO com voce. '''
print("{:=^70}".format('\033[1:34:40m BEM VINDO AO JOKENPO PYTHON \033[m'))
print('''Your options : 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

user = int(input('Qual sua jogada?'))
if user <0 or user >= 3:
    print('Jogada INVALIDA. Tente novamente.')
    exit()
print('O computador jogou {}.'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[user]))

if computador == 0: #Computador jogou PEDRA
    if user == 0:
        print('EMPATE')
    elif user == 1:
        print('O JOGADOR VENCEU!')
    elif user == 2:
        print('O COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVALIDA')
elif computador == 1: #Jogador jogou PAPEL
    if user == 0:
        print('O COMPUTADOR VENCEU!')
    elif user == 1:
        print('EMPATE')
    elif user == 2:
        print('O JOGADOR VENCEU!')
    else:
        print('JOGADA INVALIDA')
elif computador == 2: #Computador jogou TESOURA.
    if user == 0:
        print('O JOGADOR VENCEU!')
    elif user == 1:
        print('O COMPUTADOR VENCEU!')
    elif user == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
else:
    print('Jogada Invalida')