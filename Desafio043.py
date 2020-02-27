"""Desenvolva uma logica que leia o peso e altura de uma pessoa,calcule seu IMC e mostre seu status de acordo com a tabela abaixo.
-Abaixo de 18.5 : Abaixo do peso.
-Entre 18.5 e 25 : Peso Ideal.
-De 25 ate 30 : Sobrepeso.
-De 30 ate 40 : Obesidade.
-Acima de 40 : Obesidade morbida."""
print('\033[1:34:40m IMC - CALCULATOR  \033[m')

peso = float(input('Insira o seu PESO em KG : '))
altura = float(input('Insira sua ALTURA em M utilisando "," : '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Voce esta abaixo do peso.')
elif imc < 25:
    print('Voce esta no peso ideal. Parabens.')
elif imc < 30:
    print('Voce esta na categoria de Sobrepeso. Faca uma dieta ;)')
elif imc < 40:
    print('Voce esta na categoria de Obesidade. Uma dieta e exercicios sao uma boa opcao. ')
else:
    print('ATENCAO. Procure um medico. Obesidade morbida.')