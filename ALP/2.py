import os

def loginadm():
    os.system('clear')
    print("Digite seu RA e senha:")
    login = input("\033[31mRA: \033[0m")
    senha = input("\033[31mSenha: \033[0m")
    with open("cadastro_adm.txt", "r") as arquivo:#ABRINDO ARQUIVO 
        linhas = arquivo.readlines()
    for linha in linhas:
        ra, info = linha.split("[")#SPLIT É UTILIZADO PARA MANIPULAR A VARIAVEL
        ra = ra.strip()#STRIP É UTILIZADO PARA RETORNAR A ORIGEM DA STRING MANIPULADA 
        info = info.strip()
        senha_armazenada, nome_completo = info.split("]")
        if ra == login and senha == senha_armazenada:#COMPARANDO RA E SENHA ARMAZENADA 
            os.system('clear')
            print("\033[31mLogin realizado com sucesso!\n\033[0m")
            return True
        
        
    os.system('clear')
    print("\033[37m\033[41mLogin ou senha errada.\033[0m")
    return False


def loginusu():
    os.system('clear')
    print("Digite seu RA e senha:")
    login = input("\033[31mRA: \033[0m")
    senha = input("\033[31mSenha: \033[0m")
    with open("cadastro_usu.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    for linha in linhas:
        ra, info = linha.split("[")
        ra = ra.strip()
        info = info.strip()
        senha_armazenada, nome_completo = info.split(",")
        if ra == login and senha == senha_armazenada:
            os.system('clear')
            print("\033[31mLogin realizado com sucesso!\n\033[0m")
            return True
    os.system('clear')
    print("\033[37m\033[41mLogin ou senha errada.\033[0m")
    return False

def adicionarcadastro():
    login = input("\033[31mDigite o seu RA: \033[0m")
    senha = input("\033[31mDigite sua senha: \033[0m")
    nomecompleto = input("\033[31mDigite seu nome completo: \033[0m")
    cadastro = f"{login}[{senha},{nomecompleto}]\n"
    with open("cadastro_usu.txt", "a") as arquivo:
        arquivo.write(cadastro)
    os.system('clear')
    print("\033[31mLogin adicionado com sucesso! \n\033[0m")


def alterarsenha():
    login = input("\033[31mDigite seu RA para alterar a senha: \033[0m")
    with open("cadastro_usu.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    for i in range(len(linhas)):
        if linhas[i].startswith(login):
            senha = input("\033[31mDigite sua nova senha: \033[0m")
            linha_split = linhas[i].split("[")
            if len(linha_split) > 1:
                nomecompleto = linha_split[1].split(",")[1]
                linhas[i] = f"{login}[{senha},{nomecompleto}"
                with open("cadastro_usu.txt", "w") as arquivo:
                    arquivo.writelines(linhas)
                os.system('clear')
                print("\033[31mSenha alterada com sucesso! \n\033[0m")
                return
    print("\033[37m\033[41m RA não encontrado.\033[0m")
