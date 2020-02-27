#Desafio 036 - Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
# - O programa vai perguntar, o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# - Calcule o valor da prestacao mensal sabendo que 30% do salario nao podera se excedido ou entao seu emprestimo sera negado.# Welcome screen in Yellow!
print(60*'\033[1:33m=\033[m')
print('\033[1:33m ------- Bem vindo ao simulador de fincanciamentos!---------\033[m')
print(60*'\033[1:33m=\033[m')

#Input, first phase of the code.
housevalue = float(input('Insira aqui o valor da casa : '))
salary = float(input('Insira aqui o seu salario : '))
yearstopay = int(input('Insira aqui em quantos anos deseja pagar : '))

amounthpermonth = housevalue / (yearstopay * 12)

if (salary * 30 / 100) <= amounthpermonth:
    print('\033[1:31mSeu emprestimo foi negado! Sorry!\033[m ')
else:
    print('\033[1:32mSeu emprestimo foi aprovado! Parabens ;)\033[m')