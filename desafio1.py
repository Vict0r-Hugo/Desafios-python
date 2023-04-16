print ('Bem-vindoa a loja do Victor Hugo')
v = float(input('Qual o valor do produto?'))
q = int(input('Qual a quantidade?'))
res = (v * q)
print('O valor sem o frete foi {:.2f}' .format(res))
if (0 <= q < 11):
    fin = (res + 30.00)
    print('O valor com frete foi {:.2f}' .format(fin))
elif (11 <= q < 101):
    fin = (res + 60.00)
    print('O valor com frete foi {:.2f}' .format(fin))
elif (101 <= q < 1001):
    fin = (res + 120.00)
    print('O valor com frete foi {:.2f}' .format(fin))
else:
    fin = (res + 240.00)

print('O valor com frete foi {:.2f}' .format(fin))
