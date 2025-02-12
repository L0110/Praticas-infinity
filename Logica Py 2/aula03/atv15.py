#15
deposito = ["Calça","Short","Camisa","Short"]
print(deposito)
produto = input("Qual item deseja excluir?: ").strip().title()
backup = deposito.pop(deposito.index(produto))
print("Depois: ",deposito)
print("Backup: ",backup)
print("Quantidade de shorts: ", deposito.count("Short"))
