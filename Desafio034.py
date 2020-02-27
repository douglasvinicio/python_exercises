salario = int(input('Digite o salario do funcionario : '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 /100 )

print('O novo salario e de R${}'.format(novo))