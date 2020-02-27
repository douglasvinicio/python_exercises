"""039 - Faca um programa que leia o ano de nascimento de um jovem e informe,de acordo com sua idade:
- Se ele ainda vai se alistar ao servico militar.
- Se e a hora de se alistar.
-Se ja passou do tempo do alistamento.
Seu programa deveram tambem o tempo que falta ou que passsou do prazo"""

from datetime import date
print('\033[1:33m-----Vamos checar como se encontra seu estado para o alistamento militar.-----\033[m ')

print('''SEXO :
[1] MASCULINO
[2] FEMININO''')
sexo = int(input("Selecione uma das duas opcoes : "))
if sexo == 1:
    anonascimento = int(input('\033[1:36mDigite o seu ano de nascimento :\033[m '))
    ano = date.today().year
    idade = ano - anonascimento
    if idade < 18:
        print('Voce tem que se alistar quando completar 18 anos. Ainda faltam {} anos.'.format(18-idade))
    ano1 = ano + (18 - idade)
    print('O seu alistamento sera no ano de {}.'.format(ano1))
    if idade == 18:
        print('Esta na hora de se alistar. Dirija-se a junta militar mais proxima. Good luck!')
    else:
        print('Ja passou do tempo de se alistar.Voce tinha que ter se alistaod a {} anos atras.'.format(idade - 18))
    ano2 = ano - (idade-18)
    print('Seu ano de alistamento foi o ano de {}.'.format(ano2))

elif sexo == 2:
    print('O alistamento militar e exclusivo para o sexo masculino.')

else:
    print('Opcao invalida tente novamente.')