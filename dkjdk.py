from ast import Break


subtotal = 0 # Acumulador
print('Bem vindo a sorveteria do Victor Hugo Crisostomo')
print(
        '''
--------------------------------------------------Cardápio----------------------------------------------------
|Código	    Descrição              (500 ml) Tamanho P      (1000 ml) Tamanho M     (2000 ml) Tamanho G       |
|TR         Sabores Tradicionais     R$ 6,00                 R$ 10,00                 R$ 18,00               |
|ES         Sabores Especiais        R$ 7,00                 R$ 12,00                 R$ 21,00               |
|PR         Sabores Premium          R$ 8,00                 R$ 14,00                 R$ 24,00               |
--------------------------------------------------------------------------------------------------------------

'''
)
while True: 
    tamanho = str(input('Qual o tamanho desejado (P/M/G)?')).upper()
    sabor = str(input('Entre com o codigo do sabor desejado(TR/ES/PR):')).upper()
    if tamanho == 'P' and sabor == 'TR':
        subtotal += 6.00
        print ('Você escolheu o sabor Tradicional pequeno, de R$6,00!')
    elif tamanho == 'M' and sabor == 'TR':
        subtotal += 10.00
        print ('Você escolheu o sabor Tradicional medio , de R$10,00!')
    elif tamanho == 'G' and sabor == 'TR':
        subtotal += 18.00
        print ('Você escolheu o sabor Tradicional grande de R$18,00!')
    elif tamanho == 'P' and sabor == 'ES':
        subtotal += 7.00
        print ('Você escolheu o sabor especial pequeno, de R$7,00!')
    elif tamanho == 'M' and sabor == 'ES':
        subtotal += 12.00
        print ('Você escolheu o sabor especial medio de R$12,00!')
    elif tamanho == 'G' and sabor == 'ES':
        subtotal += 21.00
        print ('Você escolheu o sabor especial grande de R$21,00!')
    elif tamanho == 'P' and sabor == 'PR':
        subtotal += 8.00
        print ('Você escolheu o sabor premium pequeno, de R$8,00!')
    elif tamanho == 'M' and sabor == 'PR':
        subtotal += 14.00
        print ('Você escolheu o sabor premium medio de R$14,00!')
    elif tamanho == 'G' and sabor == 'PR':
        subtotal += 24.00
        print ('Você escolheu o sabor premium grande de R$24,00!')
    else:
        print('TAMANHO OU CODIGO INVALIDOS !!!')
        continue 
    cont = str(input('Deseja pedir mais alguma coisa(S/N)')).upper()
    if cont == 'S':
        continue
    else:
        print('O valor total a ser pago é {:.2f}' .format(subtotal))
        break