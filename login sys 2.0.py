import os
from random import * 
from time import * 
from sys import *
#campos para armazenar dados temporários
user = []
id = []
confirmar2 = []
confirmar3 = []
#gerando ids
for acess in range(10, 100):
    id.append(acess)
    ids = choice(id)
    prova = ids

#1º print
print('Criar ou Entrar ?')
#criando a repetição principal
while True:
    #Opções pro usuário 1
    pergunta = str(input('Se deseja criar um usuário digita s, se ja tem uma conta digite n: '))

    #caso o Usuário digite s
    if pergunta == 's':
        nome = str(input('Nome: '))
        if nome == '':
            print('Campo vazio, Encerrando o programa!')
            sleep(2)
            exit()
        
        #Obrigando o Usuário a Digitar a Senha e a Confrimação
        senha = input('Senha: ')
        if senha == '':
             print('Campo vazio, Encerrando o programa!')
             sleep(2)
             exit()


        else:
            confirmar = input('Digite a senha novamente: ')
            if confirmar == '':
                 print('Campo vazio, Encerrando o programa!')
                 sleep(2)
                 exit()           
        
        #se a confirmação não for igual a senha     
        if confirmar != senha:
            confirmar2 = input('Restam apenas 1 Tentativas, digite a senha correta: ')
            
            if confirmar2 != senha:
                confirmar3 = input('Última Tentaviva, Digite a Senha correta pela última vez: ')
                if confirmar3 != senha:
                    print('Tentativas esgotadas, Acesso Negado!')
                    sleep(2.5)
                exit()

        #caso a confirmação seja igual a senha
        if confirmar == senha:
            new = nome, senha, ids
            user.append(new)
            os.system('cls')

            print('bem-vindo(a)! Sr(a) {} o seu número de acesso é {}.'.format(nome, ids))
            print('estes são seus dados!\nNome: {}\nSenha: {}\nO número de Acesso é: {}'.format(nome, senha, ids))

        
         #caso a confirmação2 seja igual a senha
        if confirmar2 == senha:
            new = nome, senha, ids
            user.append(new)
            os.system('cls')

            print('bem-vindo(a)! Sr(a) {} o seu número de acesso é {}.'.format(nome, ids))
            print('estes são seus dados!\nNome: {}\nSenha: {}\nO número de Acesso é: {}'.format(nome, senha, ids))


          #caso a confirmação3 seja igual a senha
        if confirmar3 == senha:
            new = nome, senha, ids
            user.append(new)
            os.system('cls')

            print('bem-vindo(a)! Sr(a) {} o seu número de acesso é {}.'.format(nome, ids))
            print('estes são seus dados!\nNome: {}\nSenha: {}\nO número de Acesso é: {}'.format(nome, senha, ids))
                                    
        #perguntando se o usuário deseja continuar
        stop = str(input('Quer continuar? (S/N) '))
        #caso o usuário digite n
        if stop == 'n':
            sleep(1)
            os.system('cls')
            for i in range(1, 6, 1):
                sleep(1)
                os.system('cls')
                sleep(1)
                print('O programa encerra em {}'.format(i))
            sleep(1)
            print('Programa Encerrado.')
            sleep(.40)        
            exit()
        #caso o usuário digite s
        else:
            print('Limpando O Ambiente --' * 2)
            sleep(1)
            os.system('cls')
                    
    #caso o usuario digite n(ou seja se ja tem uma conta)
    if pergunta == 'n':
        entrar = int(input('Digite seu número de acesso:  '))
        #se o número de acesso digitado não for igual ao número de acesso gerado pra ele
        if entrar != ids:
            #dando a opção de recuperar o número de acesso do usuário
            recuperar = input('Este usuário não existe. Deseja Recuperar seu Número de acesso? (S/N) ')
            #caso o usuário aceite recuperar
            if recuperar == 's':
                #pedindo pro usuário confirmar o Nome dele, pra recuperar o Nº de Usuário
                cnome = input('Confirme seu Nome de Usuário: ')
                #se o usuário digitar o nome dele 
                if cnome == nome:
                    os.system('cls')
                    print('Seu número de acesso é {}, recuperado com seucesso!'.format(ids))
                    print('Bem-vindo(a) {}'.format(nome))
                
                #perguntando se o usuário quer continuar
                stop = str(input('Quer continuar? (S/N) '))
                #caso o usuário digite n(ou quer parar o programa)
                if stop == 'n':
                    sleep(1)
                    os.system('cls')
                    for i in range(1, 6, 1):
                        sleep(1)
                        os.system('cls')
                        sleep(1)
                        print('O programa encerra em {}'.format(i))
                    sleep(1)
                    print('Programa Encerrado.')
                    sleep(.40)        
                    exit()
                #se ele digitar s (ou continuar o programa)
                else:
                    os.system('cls')
                #se o nome de confirmação para a recuperação não for igual ao nome de usuário dele
                if cnome != nome:
                    print('Este Nome de Usuário não Existe! Crie uma conta')
            
        #se o nome de usuário digitado for igual ao número de acesso gerado pra ele
        if entrar == prova:
            print('Bem-vindo(a) {}'.format(nome))

        #perguntando se o Usuário deseja continuar
        stop = str(input('Quer continuar? (S/N) '))
         #caso o usuário digite n(ou quer parar o programa)
        if stop == 'n':
            sleep(1)
            os.system('cls')
            for i in range(1, 6, 1):
                sleep(1)
                os.system('cls')
                sleep(1)
                print('O programa encerra em {}'.format(i))
            sleep(1)
            print('Programa Encerrado.')
            sleep(.40)        
            exit()
         #se ele digitar s (ou continuar o programa)
        else:
            os.system('cls')

