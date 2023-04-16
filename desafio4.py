listafuncionarios = []
#---------------Cadastrar funcionarios---------------
def cadastrar_funcionarios(id):
    print('bem vindo ao cadastro de funcionarios')
    print('O ID do funcionario a ser cadastrado é:{}' .format(id))
    nome = input('Insira o nome do novo funcionario:')
    setor = input('Insira o setor do funcionario:')
    salario = float(input('Insira o salário do funcionario:'))
    dicionariofuncionario = {
    'id' : id,
    'nome' : nome,
    'setor' : setor,
    'salario' : salario
    }
    listafuncionarios.append(dicionariofuncionario.copy())
#-------------------fim do cadastro------------------

#---------------consultar funcionarios---------------
def consultar_funcionarios():
    print('bem-vindo a consulta de funcionarios')
    while True:
        try:
            opconsulta = int(input('''1)	Consultar Todas as Funcionários
2)	Consultar Funcionário por Id
3)	Consultar Funcionário(s) por Setor
4)	Retornar 
        '''))
        
            if (opconsulta == 1):
                print('Bem vindo a consulta Geral!')
                #selecionar cada dicionario da lista
                for funcionario in listafuncionarios:
                    #selecionar cada conjunto key : value do dicionario
                    for key, value in funcionario.items():
                        print('{} : {}' .format (key,value))
            
            elif (opconsulta == 2):
                print('Bem vindo a consultageral por ID!')
                idconslulta = int(input('Insira o ID desejado: '))
                for funcionario in listafuncionarios: #selecionar cada dicionario da lista
                    if (funcionario['id'] == idconslulta ):
                        for key, value in funcionario.items():
                            print('{} : {}' .format (key,value))
            
            elif (opconsulta == 3):
                print('Bem vindo a consulta por setor!')
                setorconslulta = input('Insira o setor desejado: ')
                for funcionario in listafuncionarios: #selecionar cada dicionario da lista
                    if (funcionario['setor'] == setorconslulta ):
                        for key, value in funcionario.items():
                            print('{} : {}' .format (key,value))
            
            elif (opconsulta == 4):
                return
            else:
                print('Insira um codigo valido!!!')
                continue
        except ValueError:
            print('Insira um codigo valido!!!')
            continue

#-------------------fim da consulta------------------

#---------------remover funcionarios---------------
def remover_funcionario():
    print('bem vindo ao removedor de funcionarios')
    idconslulta = int(input('Insira o ID desejado: '))
    for funcionario in listafuncionarios: #selecionar cada dicionario da lista
        if (funcionario['id'] == idconslulta ):
            for key, value in funcionario.items():
                listafuncionarios.remove(funcionario)
#-------------------fim da remoção------------------

#-----------------------MENU------------------------
print('Bem-vindo ao controle de funcionarios do Victor Hugo')
matricula = 0
while True:
    try:
        opcao = int(input('''1.	Cadastrar Funcionário
2.	Consultar Funcionários(s) 
3.	Remover Funcionário
4.	Sair
>>> '''))
        if (opcao == 1):
            matricula += 1
            cadastrar_funcionarios(matricula)
        elif (opcao == 2):
            consultar_funcionarios()
        elif (opcao == 3):
            remover_funcionario()
        elif (opcao == 4):
            print('Programa finalizado')
            break
        else:
            print('Insira um codigo valido!!!')
            continue
    except ValueError:
        print('Insira um codigo valido!!!')
        continue
#---------------------FIM MENU----------------------