"""
 Crie um dicionário que irá armazenar informações de um contato, 
 incluindo o nome, o telefone e o email. Peça ao usuário para fornecer 
 esses dados, solicitando que ele insira o nome do contato, o número de 
 telefone e o endereço de email. Após coletar todas as informações necessárias, 
 exiba o conteúdo do dicionário, mostrando todas as informações do contato 
 inserido pelo usuário.
"""
import os

contatos = {"nome":[],"tel":[],"email":[]}

while True:
    print("*"*30,"Cadastro","*"*30)
    #----------------------
    n = None
    t = None
    e = None
    while n == None: 
        n = str(input("Nome: "))
    while t == None: 
        t = int(input("Telefone: "))
    while e == None: 
        e = str(input("E-Mail: "))
    #----------------------
    contatos["nome"].append(n)
    contatos["tel"].append(t)
    contatos["email"].append(e)
    #----------------------
    fim = None
    while fim != "Y" and fim != "N":
        fim = input("Deseja Continuar? (Y/N)").upper().strip()
        if fim == "Y":
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif fim == "N":
            break
    if fim == "N": break

#----------------------
print("*"*30,"Exibição","*"*30)
for i in range(len(contatos["nome"])):
    print("-"*60)
    print("Nome:", contatos['nome'][i])
    print("Telefone:",contatos['tel'][i])
    print("email: ",contatos['email'][i])
    