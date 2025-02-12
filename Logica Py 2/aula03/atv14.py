#14
#criando uma lista
frutas = ("maçã","banana","laranja","abacaxi")

#metodo index():   retorna o indice da primeira ocorrencia do elemento especificado
indice_laranja = frutas.index("laranja")
print("ìndice da laranja:", indice_laranja) # Saída: 2

#metodo count():   retorna a quantidade de ocorrencias do elemento especificado
quantidade_bananas = frutas.count("banana")
print("quantidade de bananas:", quantidade_bananas) # Saída: 1

#Desenpacotando uma tupla
maca,banana,laranja,abacaxi = frutas
print("Fruta 1:", maca)
print("Fruta 2:", banana)
print("Fruta 3:", laranja)
print("Fruta 4:", abacaxi)

print(frutas)
