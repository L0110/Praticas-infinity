"""
Crie um programa que receba uma lista de números e
remova todas as duplicatas usando um conjunto (set). Em
seguida, exiba a lista original e a lista sem duplicatas.
"""

import random
#-----------------------
listaN = []
novaListaN = []
#-----------------------
for n in range(1,20):
    listaN.append(random.randint(1,8))
#-----------------------    
novalListaN = set(listaN)
#-----------------------
print(listaN)
print(novalListaN)