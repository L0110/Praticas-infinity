#01__________________________________________________________________________________
"""
Crie um conjunto vazio chamado frutas e adicione as
seguintes frutas a ele:"maçã","banana","uva","laranja" e "morango". 
Em seguida, imprima o conjunto.
"""

frutas = {"maçã","banana","uva","laranja","morango"}
print(frutas)

#02__________________________________________________________________________________
"""Verifique se a fruta "banana" está presente no conjunto frutas e imprima o resultado."""

for fruta in frutas:
    if (fruta == "banana"):
        print("Banana está na lista de frutas")
        break
    else:
        print(".")
else:
    print("Banana não encontrada")

#-----------------
teste = {"banana"}
print(frutas.intersection(teste))