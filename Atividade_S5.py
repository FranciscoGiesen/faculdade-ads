#Francisco Enzo Giesen - ADS
from time import sleep
print(10*'=','Ola, Seja Bem Vindo',10*'=')
menu = 0 # Valor inicial para o Menu
estudantes = [] #Lista vazia criada para guardar o nome dos estudantes
dic_estudante = {'Nome' : 'Insira', 'Cpf' : 'insiracpf', 'Codigo' : 1 }
while True:
    try:
        menu = int(input('''Escolha uma opção:       
[1] Gerenciar Estudantes
[2] Gerenciar Disciplina
[3] Gerenciar Professores
[4] Gerenciar Turmas
[5] Gerenciar Matriculas
[6] Sair

Informe a opção desejada: '''))
        if 1 <= menu < 6:
            print('Processando...')
            sleep(1)
        elif menu == 6:
            print('Encerrando...')
            sleep(2)
            print('Programa encerrado.')
            break
        else:
            print('Opção invalida, tente novamente')
            continue
        if 1 <= menu <= 6:
            print(f'Você selecionou a opção {menu}, abrindo o menu de operações...')
        #sleep(1)
    except:
        print(30 * '-')
        print('Valor inválido, tente novamente.')
        print(30 * '-')
        continue
#Aqui eu Utilizei o while true para fazer o laço Menu que "comandará" o resto do código, sempre voltando pra ele após o break dos outros laços.
#Utilizei o Try e o Except para se o usuário escrever uma string ou um valor indévido o código não de erro e continue funcionando.
    if menu == 1:
        while True:
            try:
                    print(10*'*',f'MENU DE OPERAÇÕES [ESTUDANTES]',10*'*')
                    op_est = int(input(''' Escolha uma opção:                   
[1] Incluir
[2] Listar
[3] Atualizar
[4] Excluir.
[5] Voltar ao menu principal
 
Informe a opção desejada: '''))
                    if op_est == 1:
                        print('=-' * 10, 'Inclusão', '=-' * 10)
                        dic_estudante['Nome'] = input('Insira o nome do estudante: ')
                        dic_estudante['Cpf'] = input('Insira o CPF do estudante: ')
                        dic_estudante['Codigo'] = int(input('Insira o codigo do estudante: '))
                        estudantes.append((dic_estudante.copy()))
                    elif op_est == 2:
                        print('=-' * 10, 'Listagem', '=-' * 10)
                        if estudantes == []:
                            print('Não há estudantes cadastrados.')
                        else:
                            print(f'{ estudantes }')
                    elif op_est == 3:
                        print('=-'*10, 'Atualização', '=-'*10)
                        codestu = int(input('Digite o código do estudante que deseja atualizar: '))
                        for estudante in estudantes: #O for estudante in estudantes serve para rodar todos os dicionarios estudantes procurando oque tiver o codigo desejado
                            if estudante.get('Codigo') == codestu: #se tiver ele vai fazer o processo e substituir o conteudo do dicionario.
                                estudante['Nome'] = input('Insira o nome do estudante: ')
                                estudante['Cpf'] = input('Insira o CPF do estudante: ')
                                estudante['Codigo'] = int(input('Insira o codigo do estudante: '))
                                break
                            else:
                                print('Estudante não encontrado.')


                    elif op_est == 4:
                        print('=-'*10, 'Exclusão', '=-'*10)
                        codestuda = int(input('Digite o código do estudante que você deseja excluir: '))
                        for estudante in estudantes:
                            if estudante.get('Codigo') == codestuda:
                                estudantes.remove(estudante)
                                print('Estudante removido.')
                                break
                            else:
                                print('Estudante não encontrado.')
                                break
                    elif op_est == 5:
                        print('Voltando...')
                        sleep(1)
                        break
            except ValueError:
                print(30 * '-')
                print('Valor inválido, tente novamente.')
                print(30 * '-')
    if menu == 2:
        while True:
            try:
                    print(10*'*',f'MENU DE OPERAÇÕES [DISCIPLINAS]',10*'*')
                    op_dis = int(input(''' Escolha uma opção:
[1] Incluir
[2] Listar
[3] Atualizar
[4] Excluir.
[5] Voltar ao menu principal 

Informe a opção desejada: '''))
                    #Criei variaveis chamadas op + abreviações do que se esta operando para todos os 5 submenus, utilizando da mesma logica
                    # Se o usuário escolher n numeros ele vai ler e vai realizar x função.
                    if op_dis == 1:
                        print('EM DESENVOLVIMENTO')
                    elif op_dis == 2:
                        print('EM DESENVOLVIMENTO')
                    elif op_dis == 3:
                        print('EM DESENVOLVIMENTO')
                    elif op_dis == 4:
                        print('EM DESENVOLVIMENTO')
                    elif op_dis == 5:
                        print('Voltando...')
                        sleep(1)
                        break
            except:
                print('Valor Invalido')
    try:
        if menu == 3:
            while True:
                    print(10*'*',f'MENU DE OPERAÇÕES [PROFESSORES]',10*'*')
                    op_pro = int(input(''' Escolha uma opção:                   
[1] Incluir
[2] Listar
[3] Atualizar
[4] Excluir.
[5] Voltar ao menu principal
 
Informe a opção desejada: '''))
                    if op_pro == 1:
                        print('EM DESENVOLVIMENTO')
                    if op_pro == 2:
                        print('EM DESENVOLVIMENTO')
                    if op_pro == 3:
                        print('EM DESENVOLVIMENTO')
                    if op_pro == 4:
                        print('EM DESENVOLVIMENTO')
                    if op_pro == 5:
                        print('Voltando...')
                        sleep(1)
                        break
    except ValueError:
        print(30 * '-')
        print('Valor inválido, tente novamente.')
        print(30 * '-')
    try:
        if menu == 4:
            while True:
                if menu == 4:
                    print(10*'*',f'MENU DE OPERAÇÕES [TURMAS]',10*'*')
                    op_tur = int(input(''' Escolha uma opção:                 
[1] Incluir
[2] Listar
[3] Atualizar
[4] Excluir.
[5] Voltar ao menu principal
 
Informe a opção desejada: '''))
                if op_tur == 1:
                    print('EM DESENVOLVIMENTO')
                if op_tur == 2:
                    print('EM DESENVOLVIMENTO')
                if op_tur == 3:
                    print('EM DESENVOLVIMENTO')
                if op_tur == 4:
                    print('EM DESENVOLVIMENTO')
                if op_tur == 5:
                    print('Voltando...')
                    sleep(1)
                    break
    except ValueError:
        print(30 * '-')
        print('Valor inválido, tente novamente.')
        print(30 * '-')
    try:
        if menu == 5:
            while True:
                    print(10*'*',f'MENU DE OPERAÇÕES [MATRICULAS]',10*'*')
                    op_mat = int(input(''' Escolha uma opção:                   
[1] Incluir
[2] Listar
[3] Atualizar
[4] Excluir.
[5] Voltar ao menu principal 

Informe a opção desejada: '''))

                    if op_mat == 1:
                        print('EM DESENVOLVIMENTO')
                    if op_mat == 2:
                        print('EM DESENVOLVIMENTO')
                    if op_mat == 3:
                        print('EM DESENVOLVIMENTO')
                    if op_mat == 4:
                        print('EM DESENVOLVIMENTO')
                    if op_mat == 5:
                        print('Voltando...')
                        sleep(1)
                        break
    except ValueError:
        print(30 * '-')
        print('Valor inválido, tente novamente.')
        print(30 * '-')
    #Em Todos os submenus eu utilizei do while pra só sair do submenu caso a opção 5 for selecionada.
    #Também usei try e except em todos os submenus para caso for digitado um valor indevido o codigo não dê erro e continue sua programação normal.





#print(f'Você escolheu a opção {submenu}, opção valida' if menu >= 1 and menu < 6 else 'Opção invalida')'''
