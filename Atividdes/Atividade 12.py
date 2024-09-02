"""Soma de Números com Desconto:
Peça ao usuário para inserir 5 preços de produtos. Use um laço for para
calcular o total. Aplique um desconto de 10% se o total ultrapassar 100 e
interrompa o loop com break."""

print("Soma de Números com Desconto")
print("Insira o valor de 5 produtos: ")
soma = 0
for i in range (5):
    print("Produto ",i+1,":",end='')
    produto = float(input(""))
    soma += produto
    if soma > 100:
        desc = soma*0.1
        total = soma - desc
        print(f"Total: R$ {soma}\nDesconto: R$ {desc}")
        print(f"Total com desconto: R$ {total}")
        break
else:
    print(f"Total: R$ {soma}")


        