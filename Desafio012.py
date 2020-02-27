p1 = float(input('Vamos calcular o desconto do seu produto? Insira aqui o preco:'))

# first code : d1 = 0.05
#s = d1*p1
#p2 = p1-s

#new code downhere lokking at the excercise
s = p1 - (p1 * 5/100)
s2 = p1 * 5/100

print('O seu desconto e de {:.2f}'.format(s2))
print('O valor do seu produto com desconto e {:.2f}'.format(s))


