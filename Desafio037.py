num = int(input('Digite um numero inteiro : '))
print('''Escolha uma das opcoes para conversao : 
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
option = int(input('Sua opcao : '))

if option == 1 :
    print('O valor {} convertido para BINARIO e igual a {}.'.format(num,bin(num)[2:]))
elif option == 2:
    print('O valor {} convertido para OCTAL e de {}.'.format(num,oct(num)[2:]))
elif option == 3:
    print('O valor {} convertido para HEXADECIMAL e igual a {}.'.format(num,hex(num)[2:]))
else:
    print('A opcao digitada e invalida.')

