# Recebe um número do usuário
numero = int(input("Digite um número: "))

# Inicializa o contador
contador = 1

# Exibe os dois próximos números à frente do número fornecido
while contador <= 2:
    numero += 1
    print(numero)
    contador += 1