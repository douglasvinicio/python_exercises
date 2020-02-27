'''Crie um programa que calcule a soma entre todos os numeros impares
que sao multiplos de rees e que se encontram no intervalo de 1 ate 500.'''
sum = 0
for count in range(0,501):
    if count % 3 == 0:
        sum = sum + count
print(sum)

