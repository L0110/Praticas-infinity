"""
 Importe o módulo 'os' e use a função 'listdir' para listar todos os arquivos e 
 pastas presentes no diretório onde o script Python está sendo executado. A função 'listdir' 
 retornará uma lista contendo os nomes dos arquivos e pastas. Após obter essa lista, exiba cada item 
 da lista individualmente na saída do console.
"""

import os


#Definicao do caminho
caminho = 'Logica Py 2'
conteudo = os.listdir(caminho)

# Listagem de todas as pastas no camimnho
conteudo_diretorio = os.listdir(caminho)
print(f"Pastas do diretorio: {caminho}")
print("-"*60)

for i in conteudo_diretorio:
    print("- ",i)


print("-"*60)
print(f"Arquivos do diretorio: {caminho}")
print("-"*60)

#Listagem de todos os arquivos no diretorio e os subdiretorios
for item in conteudo_diretorio:
    caminho_completo = os.path.join(caminho,item)
    if os.path.isdir(caminho_completo):
        #listagem dos subdiretorios
        print("-"*60)
        print(f"- {os.path.join(caminho,item)}")
        print("."*60)
        
        subdiretorio_conteudo = os.listdir(caminho_completo)
        for subitem in subdiretorio_conteudo:
            if os.path.isfile(os.path.join(caminho_completo,subitem)):
                
                print("-- ",os.path.join(caminho_completo,subitem))
            
            elif os.path.isfile(caminho_completo):
                #listagem dos arquivos do diretorio principal

                print("- ",caminho_completo)