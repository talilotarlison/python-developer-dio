# dados usuario
nome = "João"
idade = 30
profissao = "Engenheiro"

# 1. Usando o operador %

resultado = "Nome: %s, Idade: %d, Profissão: %s" % (nome, idade, profissao)
print(resultado)

# 2. Usando o método .format()
resultado = "Nome: {}, Idade: {}, Profissão: {}".format(nome, idade, profissao)
print

# 3. Usando f-strings (Python 3.6+)
resultado = f"Nome: {nome}, Idade: {idade}, Profissão: {profissao}"
print(resultado)

# 4. Usando str.format_map()
resultado = "Nome: {nome}, Idade: {idade}, Profissão: {profissao}".format_map({'nome': nome, 'idade': idade, 'profissao': profissao})
print(resultado)