vel = int(input('Vamos calcular o valor da multa. Qual era a velocidade do carro? Digite aqui: '))
valorm = (vel - 80 )* 7

if vel >= 80:
    print ('Voce foi multado! O valor da sua multa e de R${}'.format(valorm))

else:
    print('Voce nao foi multado, o limite de velocidade maxima e 80KMh')

