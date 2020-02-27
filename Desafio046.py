#Monte um programa que mostre na tela uma contagem regressiva
# para o estouro dos fogos de articfio. De 10 a 0 com uma pausa de um segundo entre eles.
from time import sleep
for c in range(10,-1,-1):
    print(c)
    sleep(1)
sleep(1)
print('FELIZ ANO NOVO PORRA!')