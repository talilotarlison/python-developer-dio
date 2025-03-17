# conteúdo: Conjuntos em python
numeros1 = {1, 2, 3, 2}

numeros = list(numeros1)

print(numeros[0])

# Adicionando elementos a um conjunto
numeros1.add(5)
print(numeros1)  # {1, 2, 3, 5}

# Atualizando um conjunto com outro conjunto
numeros1.update({6, 7})
print(numeros1)  # {1, 2, 3, 5, 6, 7}

# Removendo um elemento de um conjunto
numeros1.remove(2)
print(numeros1)  # {1, 3, 5, 6, 7}

# Removendo um elemento de um conjunto sem gerar erro se o elemento não existir
numeros1.discard(10)
print(numeros1)  # {1, 3, 5, 6, 7}

# Removendo e retornando um elemento arbitrário de um conjunto
elemento = numeros1.pop()
print(elemento)
print(numeros1)

# Limpando todos os elementos de um conjunto
numeros1.clear()
print(numeros1)  # set()

# União de conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
uniao = conjunto1.union(conjunto2)
print(uniao)  # {1, 2, 3, 4, 5}

# Interseção de conjuntos
intersecao = conjunto1.intersection(conjunto2)
print(intersecao)  # {3}

# Diferença de conjuntos
diferenca = conjunto1.difference(conjunto2)
print(diferenca)  # {1, 2}

# Diferença simétrica de conjuntos
diferenca_simetrica = conjunto1.symmetric_difference(conjunto2)
print(diferenca_simetrica)  # {1, 2, 4, 5}

# Verificando se um conjunto é subconjunto de outro
print(conjunto1.issubset(uniao))  # True

# Verificando se um conjunto é superconjunto de outro
print(uniao.issuperset(conjunto1))  # True

# Verificando se dois conjuntos são disjuntos
print(conjunto1.isdisjoint({6, 7}))  # True