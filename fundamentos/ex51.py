# dicionarios em python
pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)

pessoa["idade"] = 29  # {"nome": "Guilherme", "idade": 29, "telefone": "3333-1234"}
print(pessoa)
# Removendo um item pelo nome da chave
del pessoa["telefone"]
print(pessoa)

# Adicionando novamente para os próximos exemplos
pessoa["telefone"] = "3333-1234"

# Usando o método get para acessar um valor
telefone = pessoa.get("telefone")
print(telefone)

# Usando o método keys para obter todas as chaves
chaves = pessoa.keys()
print(chaves)

# Usando o método values para obter todos os valores
valores = pessoa.values()
print(valores)

# Usando o método items para obter todos os pares chave-valor
itens = pessoa.items()
print(itens)

# Usando o método pop para remover um item e obter seu valor
idade = pessoa.pop("idade")
print(idade)
print(pessoa)

# Usando o método popitem para remover o último item inserido
ultimo_item = pessoa.popitem()
print(ultimo_item)
print(pessoa)

# Usando o método update para atualizar o dicionário com outro dicionário
pessoa.update({"idade": 30, "cidade": "São Paulo"})
print(pessoa)

# Usando o método clear para limpar o dicionário
pessoa.clear()
print(pessoa)