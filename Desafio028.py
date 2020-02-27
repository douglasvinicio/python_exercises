from random import random , randint
n = randint(1,5)
print('O computador acaba de escolher um numero de 1 a 5. Quer tentar adivinhar?')
n1 = int(input('Digite um numero de 1 a 5: '))
if n == n1 :
    print('Voce acertou! Congratulations!')

else:
    print('Que pena! Voce esta sem sorte!')

    print('Voce precisa escolher um numero de 1 a 5! Essas sao as regras ;)')