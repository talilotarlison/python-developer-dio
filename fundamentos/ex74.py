from datetime import datetime

data1 = datetime(2025, 3, 15, 12, 0)  # 15 de março de 2025, 12:00
data2 = datetime(2025, 3, 10, 8, 30)  # 10 de março de 2025, 08:30

diferenca = data1 - data2  # Retorna um objeto timedelta

print(diferenca)  # Saída: 5 days, 3:30:00
print(type(diferenca))  # Saída: <class 'datetime.timedelta'>
