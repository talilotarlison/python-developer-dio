# Exemplo 1: Fatiamento básico
string = "Hello, World!"
print(string[0:5])  # Saída: Hello

# Exemplo 2: Fatiar do início até um índice
print(string[:5])   # Saída: Hello

# Exemplo 3: Fatiar de um índice até o final
print(string[7:])   # Saída: World!

# Exemplo 4: Fatiar com passo
print(string[::2])  # Saída: Hlo ol!

# Exemplo 5: Fatiar com índices negativos
print(string[-6:])  # Saída: World!

# Exemplo 6: Fatiar com índices negativos e passo
print(string[::-1]) # Saída: !dlroW ,olleH