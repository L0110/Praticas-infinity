"""
UDF: (USER DEFINED FUNCTION)
"""

def saudacao1 ():
    return "Olá"

def saudacao2 (nome_usuario:str=''):
    return f"Olá {nome_usuario}"

def saudacao3 (nome_usuario:str='') -> str:
    '''
        Função saudação3(): 
        Esta função retorna uma saudação 
        personalisada ao Usuário.
        -------------------------------\n
        Argumentos:
            -Nome_usuario (str): Nome do Usuário 
            nome_usuario: Uma String
        retorna:
            -Uma String concatenada:
        Exemplo:
            print(saudacao3("Ana"))
    '''
    return f"Olá {nome_usuario}"

def saudacao4 (nome_usuario:str='Fulano') -> str:#Função sem a obrigação de entrada de dados para ser acionado
    '''
        Função saudação3(): 
        Esta função retorna uma saudação 
        personalisada ao Usuário.
        -------------------------------\n
        Argumentos:
            -Nome_usuario (str): Nome do Usuário 
            nome_usuario: Uma String
        retorna:
            -Uma String concatenada:
        Exemplo:
            print(saudacao3("Ana"))
    '''
    return f"Olá {nome_usuario}"

def saudacao5(nome='',turno=''):#O parametro não obrigatório deve ser posto or último
    return f"Olá {nome}! Tenha {turno}"


def saudacao6(turno='', nome=''):#O parametro não obrigatório deve ser posto or último
    return f"Olá {nome}! Tenha {turno}"

def saudacaoHora(a):

    if a >= 0 and a<4 or a>=19 and a<=23:
        return "Boa noite"
    elif a>=4 and a<12:
        return "Bom dia!"
    elif a>=12 and a<=18:
        return "Boa tarde"
    else:
        return "Hora inválida"