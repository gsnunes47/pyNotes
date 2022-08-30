import defs
from os import system

#Verificar a existencia do arquivo de usuários.
file = 'users.txt'
if defs.findFile(file) == False:
    defs.createFile(file)

#Criação e adição de dados do arquivo ao dicionário com login e senha.
users = dict()
with open('users.txt', 'rt') as arq:
    for l in arq:
        x = l.split(' ; ')
        x[1] = x[1].replace('\n', '')
        users[f'{x[0]}'] = f'{x[1]}'

#Login / Cadastro
while True:

    #Cadastro
    print('=' * 20)
    userLogin = str(input('''Aperte o número 5 para realizar o cadastro
Login: '''))
    if userLogin == '5':
        print('Preencha os dados para realizar o cadastro.')
        x = str(input('Login [Nome]: '))
        if x in users:
            print('Login já cadastrado.')
            print('Por favor escolha outro nome.')
            while x in users:
                x = str(input('Login [Nome]: '))
        y = str(input('Senha: '))
        defs.writeFile(file, x, y)
        users[f'{x}'] = f'{y}'
        continue

    #Login 
    elif userLogin in users:
        strike = 0
        if userLogin in users:
            while strike != 3:
                password = str(input('Senha: '))
                if password == users[f'{userLogin}']:
                    break 
                else:
                    strike += 1
                    if strike <= 2:
                        print('Senha incorreta, Tente novamente.')
                    elif strike == 3:
                        print('Você digitou a senha incorreta muitas vezes.')
                        exit()
        break
    
system('cls')
print('Login realizado com sucesso!')
print(f'Bem vindo {userLogin}.')

#Criação e identificação de arquivo de usuário
userFile = f'{userLogin}.txt'
if defs.findFile(userFile) == False:
     defs.createFile(userFile)

#Menu com opções
while True:
    defs.menu('Ver suas notas', 'Criar novas notas', 'Sair do programa')
    print()
    choice = str(input('O que você deseja fazer? '))

    if choice == '1':
        print()
        for l in open(userFile, 'rt'):
            print(l.strip())
        print()

    elif choice == '2':
        print('Escreva [171] para voltar ao menu.')
        while True:
            w = open(userFile, 'at+')
            msg = str(input('W = '))
            if msg == '171':
                w.close
                system('cls')
                break
            w.write(f'{msg}\n')
            w.close
        continue
    
    else:
        print('Até a proxima.')
        break
