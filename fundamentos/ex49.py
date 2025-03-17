# conjunto é uma coleção de elementos únicos e não ordenados

numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

# Adicionando elementos a um conjunto
numeros.add(5)
print(numeros)  # {1, 2, 3, 4, 5}


numeros1 = {1, 2, 3, 2}

numeros = list(numeros1)

print(numeros[0])

# interando sobre um conjunto
carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
