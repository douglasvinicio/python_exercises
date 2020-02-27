"""041 - A Confederacao Nacional de Natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,de acordo com idade:
- Ate 9 anos : MIRIM
- Ate 14 anos : INFANTIL
- Ate 19 anos : JUNIOR
- Ate 20 anos : SENIOR
-Acima de 20 anos : MASTER
"""


from datetime import date

print(40*'\033[1:33m=\033[m')
print('\033[1:33m***CONFEDERACAO NACIONAL DE NATACAO****\033[m')
print(40*'\033[1:33m=\033[m')

print('\033[1:34m***** CHECAR CATEGORIA DO ATLETA ******\033[m')
print(40*'\033[1:33m=\033[m')
n = int(input('Insira o ano de nascimento do atleta : '))

n2 = date.today().year - n

if n2 <= 9:
    print('O atleta faz parte da categoria MIRIM.')
elif n2 <= 14:
    print('O atleta faz parte da categoria INFANTIL')
elif n2 <= 19:
    print('O atleta faz parte da categoria JUNIOR')
elif n2 <= 20:
    print('O atleta faz parte da categoria SENIOR')
else:
    print('O atleta faz parte da categoria MASTER')