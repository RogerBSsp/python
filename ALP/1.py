import os        #Importando OS.clear para limpar as telas  
import datetime  # importando datetime para dia e hora
from funcoes_login import loginadm, loginusu, adicionarcadastro, alterarsenha
from funcoes_itens import visualizaritens, adicionaritem, alteraritem, excluiritem
while True:
    print("\033[91m" + '''
 _______ _______         _______ ______  _______ _______    _______    _______ _______ _______ ______ _______________  _______ _______   
(  ___  (  ____ |\     /(  ___  (  __  \(  ___  (  ____ \  (  ____ \  (  ____ (  ____ (  ____ (  __  \\__   __(  __  \(  ___  (  ____ \  
| (   ) | (    \| )   ( | (   ) | (  \  | (   ) | (    \/  | (    \/  | (    )| (    \| (    )| (  \  )  ) (  | (  \  | (   ) | (    \/  
| (___) | |     | (___) | (___) | |   ) | |   | | (_____   | (__      | (____)| (__   | (____)| |   ) |  | |  | |   ) | |   | | (_____   
|  ___  | |     |  ___  |  ___  | |   | | |   | (_____  )  |  __)     |  _____|  __)  |     __| |   | |  | |  | |   | | |   | (_____  )  
| (   ) | |     | (   ) | (   ) | |   ) | |   | |     ) |  | (        | (     | (     | (\ (  | |   ) |  | |  | |   ) | |   | |     ) |  
| )   ( | (____/| )   ( | )   ( | (__/  | (___) /\____) |  | (____/\  | )     | (____/| ) \ \_| (__/  ___) (__| (__/  | (___) /\____) |_ 
|/     \(_______|/     \|/     \(______/(_______\_______)  (_______/  |/      (_______|/   \__(______/\_______(______/(_______\_______(_)
''')
    print("\033[37m\033[41m             *Programa realizado por: Felipe Bezerra, Gustavo Freitas, Larissa Matsuda, Roger Santos e Suellen Donato.*                  \033[0m")
    print("menu:\n[ 1 ] - login administração.\n[ 2 ] - Login usuário.\n[ 3 ] - Sair.\n")
    opcao = int(input("\033[31mDigite a opção desejada: \033[0m"))
    
    if(opcao==1):
        if loginadm():
            while True:
                print("Menu:\n[ 1 ] - Adicionar item\n[ 2 ] - Alterar item\n[ 3 ] - Excluir item\n[ 4 ] - Visualizar itens\n[ 5 ] - Voltar\n")
                opcao = int(input("\033[31mDigite a opção desejada: \033[0m"))
                if(opcao==1):
                    os.system('clear')
                    adicionaritem()
                elif(opcao==2):
                    os.system('clear')
                    visualizaritens()
                    alteraritem()
                elif(opcao==3):
                    os.system('clear')
                    visualizaritens()
                    excluiritem()
                elif(opcao==4):
                    os.system('clear')
                    visualizaritens()
                    while True:
                        print("\033[37m\033[41m[ 1 ] para retornar.\033[0m")
                        opcao = int(input("\033[31mDigite a opção desejada: \033[0m"))
                        if (opcao==1):
                            os.system('clear')
                            break
                elif(opcao==5):
                    os.system('clear')
                    break
                else:
                    os.system('clear')
                    print("\033[37m\033[41m Opção NÃO encontrada.\033[0m")
    
    elif(opcao==2):
        os.system('clear')
        while True:
            print("menu:\n[ 1 ] - login.\n[ 2 ] - Adicionar cadastro.\n[ 3 ] - Alterar senha.\n[ 4 ] - Voltar.\n")
            opcao = int(input("\033[31mDigite a opção desejada: \033[0m"))

            if(opcao==1):
                if loginusu():
                    data_atual = datetime.date.today()
                    hora_atual = datetime.datetime.now().strftime("%H:%M")
                    visualizaritens()
                    print(f"\033[37m\033[41mItens Atualizados em: {data_atual}   Horário: {hora_atual}.\033[0m\n")
                    while True:
                        opcao = int(input("\033[31mDigite [ 1 ] - Retornar: \033[0m"))
                        if (opcao==1):
                            os.system('clear')
                            break
                        else:
                            os.system('clear')
                            print("\033[37m\033[41m Opção NÃO encontrada.\033[0m")
            elif(opcao==2):
                adicionarcadastro()

            elif(opcao==3):
                alterarsenha()

            elif(opcao==4):
                os.system('clear')
                break

            else:
                os.system('clear')
                print("\033[37m\033[41m Opção NÃO encontrada.\033[0m")
    
    
    elif(opcao==3):
        os.system('clear')
        break


    else:
        os.system('clear')
        print("\033[37m\033[41m Opção NÃO encontrada.\033[0m")
        