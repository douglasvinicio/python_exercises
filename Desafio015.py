dias = int (input('Quantos dias o carro foi alugado?'))
kms = float(input('Quantos kilometros foram rodados? '))

priced = 60
pricekm = 0.15

priced1 = dias*priced
pricekm1 = kms*pricekm

total = priced1 + pricekm1

print ('Sabendo que o preco do aluguel e de R${:.2f} e o preco a mais por KM e R${:.2f}. \n'
       'O preco total a ser pago pelo aluguel do carro e de R${:.2f}'.format(priced,pricekm,total))