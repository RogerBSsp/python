import os

def visualizaritens():
    with open("itens.txt", "r") as arquivo:
        itens = arquivo.read()
    print("Itens encontrados em poder da secretária:")
    print(itens)

def adicionaritem():
    nome = input("\033[31mDigite o nome do item: \033[0m")
    descricao = input("\033[31mDigite a descrição do item: \033[0m")
    local = input("\033[31mDigite o local onde foi achado: \033[0m")
    horario = input("\033[31mDigite o horário que o item foi achado: \033[0m")
    with open("itens.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        numero = len(linhas) + 1
    item = f"\nReferencia: {numero}\nNome: {nome}\nDescrição: {descricao}\nLocal: {local}\nHorário: {horario}\n"
    with open("itens.txt", "a") as arquivo:
        arquivo.write(item)
    os.system('clear')
    print ("\033[31mItem adicionado com sucesso! \n\033[0m")

def alteraritem():
    referencia = input("\033[31mDigite a REFERENCIA do item que deseja alterar: \n\033[0m")
    with open("itens.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    for i in range(len(linhas)):
        if linhas[i].startswith("Referencia:"):
            if linhas[i].split(":")[1].strip() == referencia:
                descricao = input("\033[31mDigite a nova descrição do item: \033[0m")
                local = input("\033[31mDigite o novo local onde foi achado: \033[0m")
                horario = input("\033[31mDigite o novo horário em que foi achado: \033[0m")
                linhas[i + 2] = f"Descrição: {descricao}\n"
                linhas[i + 3] = f"Local: {local}\n"
                linhas[i + 4] = f"Horário: {horario}\n"
                with open("itens.txt", "w") as arquivo:
                    arquivo.writelines(linhas)
                os.system('clear')
                print("\033[31mItem alterado com sucesso! \n\033[0m")
                return
            
    os.system('clear')
    print("\033[37m\033[41mItem NÃO eoncotrado.\033[0m")

def excluiritem():
    Referencia = input("\033[31mDigite a REFERENCIA do item que deseja excluir: \033[0m")
    with open("itens.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    with open("itens.txt", "w") as arquivo:
        for i in range(len(linhas)):
            if linhas[i].startswith("Referencia:"):
                if linhas[i].split(":")[1].strip() == Referencia:
                    arquivo.write("".join(linhas[:i]))
                    if i + 6 < len(linhas):
                        arquivo.write("".join(linhas[i + 6:]))
                    os.system('clear')
                    print("\033[31mItem excluído com sucesso!\n\033[0m")
                    return
    os.system('clear')
    print("\033[37m\033[41mItem NÃO eoncotrado.\033[0m")
