'''  Crie um programa em Python que simule um sistema de login. O programa deve permitir ao 
usuário três tentativas para acertar o nome de usuário e a senha corretos. Caso o usuário erre 
as credenciais, o programa deve fornecer uma mensagem informando quantas tentativas restam. Se o 
usuário acertar, uma mensagem de boas-vindas deve ser exibida, e o programa deve terminar imediatamente.'''


tentativas = 3

while tentativas > 0:
    user = input("Digite o nome de usuário: ")
    chave = input("Digite a senha: ")

    if user == "teste" and chave == "1234":
        print("Bem Vindo!")
        break
    else:
        tentativas -= 1
        print(f"Tentativas restantes: {tentativas}")

    if tentativas == 0:
        print("\n\nTentativas esgotadas")
        break