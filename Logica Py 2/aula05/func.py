def soma(a,b):
    """
    Função que calcula a soma de dois números.
    Argumentos: a (float) e b (float)
    Retorno: a soma de a e b
    Exemplo: soma(5, 3) = 8
    """
    return a+b

def media(a:float, b:float, c:float)-> float:
    """
    Função que calcula a média aritimética\n
    Argumentos: arg1, arg2, arg3, valores para cálculos\n
    Retorna: Número Real representando a média\n
    Exemlo: Média(2.5,8.10)
    """
    return (a+b+c)/3


def med(lista_notas:list)-> float:
    """
    Função que calcula a média aritimética, indendente d aquantidade de valores a serem calculados\n
    Argumentos: arg1, arg2, arg3... valores para cálculos\n
    Retorna: Número Real representando a média\n
    Exemlo: Média(2.5,8.10)
    """
    return sum(lista_notas)/len(lista_notas)

def dados(**dic_dados):
    text = ''
    for k,v in dic_dados.items():
        text += f"{k} = {v}, "
    return text



#---------------- TESTE DE MESA ----------------
"""som = list
som = [5,5,6,7,8,9,10,9.5]
print(f"média: {med(som)}")

print(dados(
    Nome = "Vinicius",
    Idade = "44",
    Endereco = "Rua Abc, 123"
    ))

print(dados(
    Idade = "23",
    Nome = "José",
    Endereco = "Rua Abc, 123"
    ))

cliente = input("Nome do cliente: ").strip().upper()
endereco = input("insira o endereco: ").strip().upper()
cpf_cli = input("insira o cpf: ").strip().upper()
idade = int(input("insira a idade: "))
print(dados(
    Nome = cliente,
    Idade = idade,
    Endereco = endereco,
    CPF = cpf_cli
    ))
"""
def concatenar_strings(*lista):
    saida = ''
    for texto in lista:
        saida += ' ' + texto
    return saida.strip()


