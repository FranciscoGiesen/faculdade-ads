#Francisco Enzo Giesen - ADS
from time import sleep
menu = 0 # Valor inicial para o Menu
m = 0
estudantes = [] #Lista vazia criada para guardar o nome dos estudantes
disciplinas = []
professores = []
turmas = []
matriculas = []
dic_estudante = {'Nome' : 'Insira', 'Cpf' : 'insiracpf', 'Codigo' : 1 }
def menuprincipal(mp):#Função pra criar o menu principal
    print(10 * '=', 'Ola, Seja Bem Vindo', 10 * '=')
    print(
        '''[1] Gerenciar Estudantes
[2] Gerenciar Disciplina
[3] Gerenciar Professores
[4] Gerenciar Turmas
[5] Gerenciar Matriculas
[6] Sair
'''
)
def incluir(lista_destino, nomeitem): #função para criar a opção incluir no sistema
    print('=-' * 10, 'Inclusão', '=-' * 10)
    try:
        nome = input(f'Digite o Nome do {nomeitem}: ')
        cpf = input(f'Digite o Cpf do {nomeitem}: ')
        codigo = int(input(f'Digite o Codigo do {nomeitem}: '))
        novoitem = {'Nome': nome, 'Cpf': cpf, 'Codigo': codigo}
        lista_destino.append(novoitem)
    except:
        print(30 * '-')
        print('Valor inválido, tente novamente.')
        print(30 * '-')
    return lista_destino
def listar(nomelistar, nomelistado):#função para criar a função listar no sistema
    print('=-' * 10, 'Listagem', '=-' * 10)
    if not nomelistar:
        print(f'não há nenhum {nomelistado} na lista.')
    else:
        print(f'{nomelistar}')
def atualizar(nome_atualizar, nomeitem):
    print('=-' * 10, 'Atualização', '=-' * 10)
    codigo = int(input(f'Digite o código do {nomeitem} que deseja atualizar: '))
    for item in nome_atualizar:
        if item.get('Codigo') == codigo:
            item['Nome'] = input('Insira o nome do estudante: ')
            item['Cpf'] = input('Insira o CPF do estudante: ')
            item['Codigo'] = int(input('Insira o codigo do estudante: '))
            break
    else:
        print(f'{nomeitem} não encontrado.')
def excluir(nomeexcluir, nomeitem):
    print('=-' * 10, 'Exclusão', '=-' * 10)
    codigo = int(input(f'Digite o código do {nomeitem} que você deseja excluir: '))
    for item in nomeexcluir:
        if item.get('Codigo') == codigo:
            nomeexcluir.remove(item)
            print(f'{nomeitem} removido.')
            break
    else:
        print('Estudante não encontrado.')
def menusecundario(nomedomenu,sobremenu,nomeminusculo):
    try: #função criada para fazer um molde de cada submenu, contendo todas as possibilidades que o menu oferece.
        while True:
            print(10 * '*', f'MENU DE OPERAÇÕES [{nomedomenu}]', 10 * '*')
            opcao = int(input(''' Escolha uma opção:                   
[1] Incluir
[2] Listar
[3] Atualizar
[4] Excluir.
[5] Voltar ao menu principal

Informe a opção desejada: '''))
            if opcao == 1:
                incluir(sobremenu, nomeminusculo)
            if opcao == 2:
                listar(sobremenu, nomeminusculo)
            if opcao == 3:
                atualizar(sobremenu, nomeminusculo)
            if opcao == 4:
                excluir(sobremenu,nomeminusculo)
            if opcao == 5:
                print('Voltando...')
                sleep(1)
                return

    except ValueError:
            print(30 * '-')
            print('Valor inválido, tente novamente.')
            print(30 * '-')



#Codigo principal
while True:
    try:
        menuprincipal(m)
        menu = int(input('Escolha uma opção: '))
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
        menusecundario('ESTUDANTES',estudantes,'estudante')
    if menu == 2:
        menusecundario('DISCIPLINAS',disciplinas,'disciplina')
    if menu == 3:
        menusecundario('PROFESSORES',professores,'professores')
    if menu == 4:
        menusecundario('TURMAS',turmas,'turmas')
    if menu == 5:
        menusecundario('MATRICULAS',matriculas,'matriculas')
    if menu == 6:
        sleep(1)
        print('Programa encerrado.')
        break








