
import datetime

# calcular  fuso horário

# Definindo os fusos horários de referência
brasil_tz = datetime.timezone(datetime.timedelta(hours=-3))  # Brasília, Brasil (UTC-3)
usa_tz = datetime.timezone(datetime.timedelta(hours=-5))  # Hora padrão do Pacífico (UTC-8)

# Data e hora atual (em UTC)
agora_utc = datetime.datetime.now(datetime.UTC)

 
# Convertendo a hora atual para os fusos horários do Brasil e dos EUA
brasil_time = agora_utc.replace(tzinfo=datetime.timezone.utc).astimezone(brasil_tz)
usa_time = agora_utc.replace(tzinfo=datetime.timezone.utc).astimezone(usa_tz)

# Exibindo os horários locais de Brasil e EUA
print(f"Hora no Brasil (Brasília): {brasil_time.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Hora nos EUA (Pacific Time): {usa_time.strftime('%Y-%m-%d %H:%M:%S')}")

