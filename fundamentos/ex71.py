from datetime import datetime

date_string = "2023-05-01"
date_obj = datetime.strptime(date_string, "%Y-%m-%d")  # Correção do formato

print(date_obj)  # Saída: 2023-05-01 00:00:00
