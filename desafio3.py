#----------- inicio da função metragem_limpeza() -----------
def metragem_limpeza():
   while True:
        try: 
            metragem_l = float(input ('Insira a metragem da casa:'))
            if (metragem_l >= 30  and metragem_l < 300):
                return 60.00 + 0.3 * metragem_l
            elif (metragem_l >= 300 and metragem_l < 700):
                return 120.00 + 0.5 * metragem_l
            else:
                print('Metragem não aceita! Só aceitamos casas maiores que 30 e menores que 700 (m²)')
                continue
        except ValueError:
            print('Digite um valor numérico')
            continue
#------------ fim da função metragem_limpeza() ------------

#----------- inicio da função tipo_limpeza() -----------

def tipo_limpeza():
    while True:
        tipo_l = input('''
        Insira o tipo de limpeza:
        B - Basica (Indicada para sujeiras semanais ou quinzenais)
        C - Completa 30% mais cara (Indicada para sujeiras antigas e/ou não rotineiras)
        >>>''')
        if (tipo_l == 'B'):
            return 1.00
        elif (tipo_l == 'C'):
            return 1.30
        else:
            print('Insira um tipo de limpeza valido')
            continue

#------------ fim da função tipo_limpeza() ------------

#----------- inicio da função adicional_limpeza() -----------
def adicional_limpeza():
    adc = 0
    while True:
        adicional_l = int(input('''Deseja mais algum adicional?
        0- Não desejo mais nada (encerrar)
        1- Passar 10 peças de roupas - R$ 10.00
        2- Limpeza de 1 Forno/Micro-ondas - R$ 12,00
        3- Limpeza de 1 Geladeira/Freezer - R$ 20,00
        >>>'''))
        if (adicional_l == 0):
            adc += 0
            return adc
            break
        elif (adicional_l == 1):
            adc += 10.00
            continue
        elif (adicional_l == 2):
            adc += 12.00
            continue
        elif (adicional_l == 3):
            adc += 20.00
            continue
        else: 
            print('Adicional invalido!')
            continue
        

#------------ fim da função adicional_limpeza() ------------

#--------------------main----------------------
print('bem-vindo a Serviços e limpeza do Victor Hugo')

metragem = metragem_limpeza()
tipo = tipo_limpeza()
adicional = adicional_limpeza()

total = (metragem * tipo + adicional)
print('Total: R${:.2f}, (metragem {:.2f} * tipo {:.2f} + adicional {:.2f})' .format (total, metragem, tipo ,adicional))

#-----------------fim da main------------------