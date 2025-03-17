from datetime import datetime, timezone

# Objeto datetime aware
dt_aware = datetime(2023, 1, 1, tzinfo=timezone.utc)
print(dt_aware.tzinfo)  # Saída: UTC

# Objeto datetime naive
dt_naive = datetime(2023, 1, 1)
print(dt_naive.tzinfo)  # Saída: None (sem fuso horário)
