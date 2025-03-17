nome = "     python"

# 1. Converter para maiúsculas
print(nome.upper())  # PYTHON

# 2. Converter para minúsculas
print(nome.lower())  # python

# 3. Capitalizar a primeira letra
print(nome.capitalize())  # Python

# 4. Trocar parte da string
print(nome.replace("py", "pyth"))  # python

# 5. Verificar se a string começa com 'py'
print(nome.startswith("py"))  # True

# 6. Verificar se a string termina com 'on'
print(nome.endswith("on"))  # True

# 7. Encontrar a posição de uma substring
print(nome.find("tho"))  # 2

# 8. Dividir a string em uma lista
print(nome.split("t"))  # ['py', 'hon']

# 9. Juntar uma lista de strings em uma única string
lista = ["py", "thon"]
print("".join(lista))  # python

# 10. Reverter a string
print(nome[::-1])  # nohtyp

print(nome.title())  # Python

print(nome.strip())  # Python


print(nome.center(20,"#"))  # Python