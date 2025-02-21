"""
[PYIA-A04] Crie uma função chamada media que receberá três números como argumentos. 
Esta função deve calcular a média aritmética desses três números. Para fazer isso, 
some os três números e, em seguida, divida o resultado por três. Por fim, a função deve 
retornar o valor da média aritmética calculada.
"""

def media(notas):
    return sum(notas)/3

notas = []

print("-"*60)
print("\t"*3,"Cálculo da média")
print("-"*60)

for i in range (1,4):
    nota = float(input(f"Nota da prova {i}: "))
    notas.append(nota)
    
print(f"A media do aluno é: { media(notas) }")