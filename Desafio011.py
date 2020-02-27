alt = int(input("Insira a altura da sua parede:"))
larg = int(input('Insira a largura da sua parede:'))
area = alt*larg

print('Sua area e de' , area,'metros quadrados')
tinta = area/2

print('Sabendo que sua area e de' , area , 'e que cada litro de tinta pinta 2m quadrados,voce vai precisar de {} litros de tinta.'.format(tinta))