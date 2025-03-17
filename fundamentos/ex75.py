from datetime import datetime

# Criando um objeto datetime naive (sem fuso horário)
data_naive = datetime(2025, 3, 15, 14, 30)

print(data_naive.tzinfo)  # Saída: None (sem fuso horário)
