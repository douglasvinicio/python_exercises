import math

n = float(input('Digite um numero real:'))

n1 = int(n)
#without lookinh the answer.
print ('O nuemro inteiro do nuemro real digitado e {}'.format(n1))
#after looking the answer.
print ('O nuemro inteiro do nuemro real digitado e {}'.format(math.trunc(n)))

