from funcs import (Automoveis, )

chevette = Automoveis(
    marca = "Chevrolet",
    cor = "Amarelo",
    maxima = 140
)

print("Cor: ", chevette.cor)
print("Ligado: ", chevette.ligado)
print("Velidade Atual: ", chevette.velo_atual)

#carro_ligado
print("Ligado", chevette.ligado)
chevette.ligar_desligar()
print("Ligado", chevette.ligado)

for x in range(15):
    chevette.acelerar(10)
    print("acelerar 10:",chevette.velo_atual)

print(chevette.velo_atual)#140


for x in range(15):
    chevette.frear(10)#0
    print("freando 10: ", chevette.velo_atual)

print("freiar 140:",chevette.velo_atual)
chevette.frear(10)#0

