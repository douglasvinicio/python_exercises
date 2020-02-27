#038 - Escreva um programa que leia um numero inteiro e mostre na tela uma mensagem :
# - O primero valor e maior
# - O segundo valor e maior
# - Nao tem valor maior, os dois sao iguais.

n1 = int(input('Digite o primeiro valor : '))
n2 = int(input('Digite o segundo valor : '))

if n1 > n2 :
    print('O primeiro valor e maior. ')
elif n2 > n1:
    print('O segundo valor e maior.')
else:
    print('Os valores sao iguais.')

