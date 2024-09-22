'''Você está desenvolvendo um programa em Python para calcular a soma dos
 números pares dentro de um intervalo determinado pelo usuário. O programa 
 deve solicitar ao usuário que insira dois números inteiros, representando o 
 início e o fim do intervalo (inclusive).
Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar 
apenas os números pares. Implemente a estrutura 'else' para exibir uma mensagem 
indicando que não há números pares no intervalo, caso seja o caso.
Ao final, exiba a soma dos números pares encontrados.'''


inicio = int(input("Insira o valor inicial do intervalo: "))
fim = int(input("Insira o valor final do intervalo: "))
soma = 0
par = 0
for i in range(inicio,fim+1):
    if (i % 2 == 0):
        soma += i
        par += 1
        print("")
else:
    if par == 0:
        print("Não há números pares no intervalo")
    print(f"\n\nSoma do intervalo: {soma}")
