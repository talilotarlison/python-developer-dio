def substituir_vogais(texto):
    vogais = "aeiou"
    novo_texto = ""
    for char in texto:
        if char in vogais:
            novo_texto += char.upper()
        else:
            novo_texto += char
    return novo_texto

# Exemplo de uso
texto = input("Digite um texto: ")
resultado = substituir_vogais(texto)
print("Texto com vogais em maiúsculo:", resultado)