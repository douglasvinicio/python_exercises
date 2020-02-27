'''044 - Elabore um programa que calcule o valor a ser pago por um produto, considenrando o seu :
Preco normal e condicao de pagamento:
-A vista dinheiro / cheque : 10% de desconto.
-A vidsta no cartao : 5% de desconto.
-em ate 2x no cartao: preco normal
-3x ou mais no cartao: 20% de juros.'''

print('{:=^70}'.format('\033[1:34:40m CELLS CELULARES \033[m'))
compra = float(input('Qual o valor da compra? Insira aqui : R$ '))
print('''FORMAS DE PAGAMENTO 
[1] a vista dinheiro / cheque
[2] a vista no cartao
[3] 2x no cartao
[4] 3x ou mais no cartao''')

opcao = int(input('Qual sera a forma de pagamento? '))
if opcao == 4:
    opcao4 = int(input('Quantas parcelas ?'))
    if opcao4 >= 3:
        print('Sua compra sera parcelada em {:.2f}x de R${:.2f} com Juros.'.format(opcao4,((compra*20)/100) + compra / opcao4))
        print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(compra , (compra * 20) / 100 + compra))
if opcao == 1:
    print('O valor para o pagamento a vista com 10% de desconto e de R${:.2f}.'.format(compra - (compra*10)/100))
if opcao == 2:
    print('O valor para pagamento a vista no cartao e de R${:.2f} com 5% de desconto.'.format(compra - (compra*5)/100))
if opcao == 3:
    print('O valor a ser pago sera de duas parcelas de R${:.2f}'.format(compra/2))
else :
    print('Opcao invalida. Tente novamente.')
