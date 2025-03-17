from datetime import datetime

# Criando um objeto datetime
data = datetime(2025, 3, 15)

# Formatando para exibir mês e ano
resultado = data.strftime("%m-%Y")

print(resultado)  # Saída: 03-2025

resultado1 = data.strftime("%B de %Y")  
print(resultado1)  # Saída: Março de 2025
