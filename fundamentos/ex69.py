from datetime import datetime
# O método correto para converter uma string em um objeto datetime em Python é strptime, que faz parte do módulo datetime.
data_string = "15/03/2025 14:30"
formato = "%d/%m/%Y %H:%M"

data_objeto = datetime.strptime(data_string, formato)
print(data_objeto)  # Saída: 2025-03-15 14:30:00
